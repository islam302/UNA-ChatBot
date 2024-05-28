import pandas as pd
from django.shortcuts import render
from .models import UploadFile, FAQ
from django.db.models import Q
from difflib import SequenceMatcher


def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)

            try:
                processed_data = save_excel_to_db(fs.path(filename))
                if processed_data:
                    return render(request, 'upload.html', {'form': form, 'processed_data': processed_data})
                else:
                    return render(request, 'upload.html', {'form': form, 'error': 'Failed to process the file.'})
            except Exception as e:
                print(f"Error processing file: {e}")
                return render(request, 'upload.html', {'form': form, 'error': 'Failed to process the file.'})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def get_answer(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')

        all_questions = UploadFile.objects.values_list('question', flat=True)
        all_answers = UploadFile.objects.values_list('answer', flat=True)

        best_match_index = -1
        best_match_score = -1
        for i, db_question in enumerate(all_questions):
            similarity_score = SequenceMatcher(None, question.lower(), db_question.lower()).ratio()
            if similarity_score > best_match_score:
                best_match_score = similarity_score
                best_match_index = i

        if best_match_score >= 0.7:
            answer = all_answers[best_match_index]
        else:
            answer = "Sorry, I couldn't find an answer to that question."

        return render(request, 'answer.html', {'question': question, 'answer': answer})
    else:
        return render(request, 'answer.html', {'error': 'Invalid request method.'})

def answer_question(request):
    if request.method == 'POST':
        user_question = request.POST.get('question', '')
        similar_questions = FAQ.objects.filter(
            Q(question__icontains=user_question) | Q(answer__icontains=user_question)
        )
        answers = [faq.answer for faq in similar_questions]
        if answers:
            return render(request, 'answer.html', {'answers': answers})
        else:
            return render(request, 'answer.html', {'answers': ['No answer found.']})
    else:
        return render(request, 'answer.html')