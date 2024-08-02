from django.shortcuts import render
from django.http import JsonResponse
from .forms import QuestionForm, UploadFileForm
from .models import QuestionAnswer
from .openai_utils import get_chatgpt_response
from .utils import get_most_similar_question, save_excel_to_db
import logging
import requests

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
    question = None

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            logging.info(f"User question: {question}")

            # Fetch all questions from the database
            all_questions = QuestionAnswer.objects.all()

            # Find the most similar question
            similar_question = get_most_similar_question(question, all_questions)

            if similar_question:
                answer = similar_question.answer
                logging.info(f"Matched question: {similar_question.question}")
                logging.info(f"Answer: {answer}")
            else:
                try:
                    # Send the question to ChatGPT API
                    chatgpt_answer = get_chatgpt_response(question)
                    logging.info(f"Response from ChatGPT: {chatgpt_answer}")
                    answer = chatgpt_answer
                except requests.exceptions.HTTPError as err:
                    logging.error(f"HTTPError: {err}")
                    return JsonResponse({"error": str(err)}, status=400)
    else:
        form = QuestionForm()

    return render(request, 'question.html', {
        'form': form,
        'answer': answer,
        'question': question if request.method == 'POST' else None
    })
