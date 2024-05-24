from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import QuestionAnswer
import fitz
from fuzzywuzzy import process


def extract_text_from_pdf(file):
    doc = fitz.open(file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_text_to_qa(text):
    lines = text.split("\n")
    questions, answers = [], []
    for line in lines:
        if line.startswith("Q:"):
            questions.append(line[2:].strip())
        elif line.startswith("A:"):
            answers.append(line[2:].strip())
    return zip(questions, answers)

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            text = extract_text_from_pdf(file)
            qa_pairs = parse_text_to_qa(text)
            for question, answer in qa_pairs:
                QuestionAnswer.objects.create(question=question, answer=answer)
            return redirect('admin:index')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def chatbot_view(request):
    if request.method == "POST":
        user_question = request.POST.get('question')
        best_match, score = process.extractOne(user_question, QuestionAnswer.objects.values_list('question', flat=True))
        if score > 80:
            answer = QuestionAnswer.objects.get(question=best_match).answer
            return render(request, 'chatbot.html', {'answer': answer})
        else:
            suggestions = process.extract(user_question, QuestionAnswer.objects.values_list('question', flat=True), limit=3)
            suggestions = [s[0] for s in suggestions]
            return render(request, 'chatbot.html', {'suggestions': suggestions})
    return render(request, 'chatbot.html')
