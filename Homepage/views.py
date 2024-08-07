from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import QuestionForm, UploadFileForm, AddQuestionForm
from .models import QuestionAnswer
from .utils import get_similar_questions, save_excel_to_db
import logging
from .utils import save_excel_to_db

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def upload_file_view(request):
    processed_data = None
    error = None
    all_data = None

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            try:
                processed_data = save_excel_to_db(uploaded_file)
            except Exception as e:
                error = str(e)
    else:
        form = UploadFileForm()

    all_data = QuestionAnswer.objects.all()

    return render(request, 'upload.html', {
        'form': form,
        'processed_data': processed_data,
        'error': error,
        'all_data': all_data
    })

def get_question_from_user(request):
    answer = None
    question = None
    similar_questions = None

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            logging.info(f"User question: {question}")

            all_questions = QuestionAnswer.objects.all()
            similar_questions = get_similar_questions(question, all_questions)

            if similar_questions:
                # Display similar questions for user to choose
                return render(request, 'question.html', {
                    'form': form,
                    'similar_questions': similar_questions,
                    'question': question
                })
            else:
                answer = 'There is no answer for this question'
    else:
        form = QuestionForm()

    return render(request, 'question.html', {
        'form': form,
        'answer': answer
    })

def select_similar_question(request, question_id):
    question_answer = get_object_or_404(QuestionAnswer, id=question_id)
    return JsonResponse({
        'question': question_answer.question,
        'answer': question_answer.answer
    })

def get_answer(request, question_id):
    try:
        question = QuestionAnswer.objects.get(id=question_id)
        response_data = {
            'question': question.question,
            'answer': question.answer,
        }
        return JsonResponse(response_data)
    except QuestionAnswer.DoesNotExist:
        return JsonResponse({'error': 'Question not found'}, status=404)

def add_question(request):
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question']
            answer_text = form.cleaned_data['answer']
            new_question = QuestionAnswer(question=question_text, answer=answer_text)
            new_question.save()
            return redirect('upload_file')
    else:
        form = AddQuestionForm()

    return render(request, 'upload.html', {'question_form': form})

def edit_question(request, id):
    question_answer = get_object_or_404(QuestionAnswer, id=id)

    if request.method == 'POST':
        form = AddQuestionForm(request.POST, instance=question_answer)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = AddQuestionForm(instance=question_answer)

    return render(request, 'edit_question.html', {'form': form})

def delete_question(request, id):
    question_answer = get_object_or_404(QuestionAnswer, id=id)
    question_answer.delete()
    return redirect('upload_file')
