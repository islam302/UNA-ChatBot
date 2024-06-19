from django.shortcuts import render
from .forms import UploadFileForm, QuestionForm
from .utils import save_excel_to_db
from .models import QuestionAnswer
from django.http import JsonResponse
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ????? ??????? ??????? ??????
tokenizer = AutoTokenizer.from_pretrained("aubmindlab/bert-base-arabert")
model = AutoModel.from_pretrained("aubmindlab/bert-base-arabert")

def get_most_similar_question(user_question, questions):
    user_question_embedding = get_embedding(user_question)
    similarities = [(question, cosine_similarity(user_question_embedding, get_embedding(question))) for question in questions]
    most_similar_question = max(similarities, key=lambda x: x[1])
    return most_similar_question if most_similar_question[1] > 0.7 else None

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def cosine_similarity(embedding1, embedding2):
    return np.dot(embedding1, embedding2.T) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))

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

    try:
        all_data = QuestionAnswer.objects.all()
    except QuestionAnswer.DoesNotExist:
        all_data = []

    return render(request, 'upload.html', {
        'form': form,
        'processed_data': processed_data,
        'error': error,
        'all_data': all_data
    })

def get_question_from_user(request):
    answer = None
    suggestion = None

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            # Check if the exact question exists
            try:
                answer = QuestionAnswer.objects.get(question__iexact=question).answer
            except QuestionAnswer.DoesNotExist:
                # If not found, find similar questions using embeddings
                all_questions = QuestionAnswer.objects.values_list('question', flat=True)
                similar_question = get_most_similar_question(question, all_questions)
                if similar_question:
                    answer = QuestionAnswer.objects.get(question=similar_question[0]).answer
                else:
                    answer = "There is no answer for this question Yet"
    else:
        form = QuestionForm()

    return render(request, 'question.html', {
        'form': form,
        'answer': answer,
        'suggestion': suggestion,
        'question': question if request.method == 'POST' else None
    })
