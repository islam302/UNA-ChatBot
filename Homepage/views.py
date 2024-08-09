from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import QuestionForm, UploadFileForm, AddQuestionForm, UnansweredQuestionForm, EditUnAnswerQuestionForm
from .models import QuestionAnswer, UnansweredQuestion
from .utils import get_similar_questions, save_excel_to_db
import logging
from django.urls import reverse

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

def get_question_from_user(request):
    answers = []  # List to store multiple answers
    question = None
    similar_questions = None

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            logging.info(f"User question: {question}")

            # Retrieve questions from both models
            answered_questions = set(QuestionAnswer.objects.values_list('question', flat=True))
            unanswered_questions = set(UnansweredQuestion.objects.values_list('question', flat=True))

            # Check if the question exists in either model
            if question in answered_questions:
                # Retrieve all answers for the question
                answers = QuestionAnswer.objects.filter(question=question).values_list('answer', flat=True)
                return render(request, 'question.html', {
                    'form': form,
                    'answers': answers,  # Pass all answers to the template
                    'question': question,
                })

            elif question in unanswered_questions:
                answer = "This question is already in our database and awaiting an answer."
                return render(request, 'question.html', {
                    'form': form,
                    'answer': answer,
                    'question': question,
                })

            # If the question doesn't exist, find similar questions
            all_questions = QuestionAnswer.objects.all()
            similar_questions = get_similar_questions(question, all_questions)

            if similar_questions:
                return render(request, 'question.html', {
                    'form': form,
                    'similar_questions': similar_questions,
                    'question': question
                })
            else:
                # Save the question in the UnansweredQuestion table if not found anywhere
                unanswered_question = UnansweredQuestion(question=question)
                unanswered_question.save()
                answer = 'There is no answer to this question at the moment. We will look into it later.'
                return render(request, 'question.html', {
                    'form': form,
                    'answer': answer,
                })
    else:
        form = QuestionForm()

    return render(request, 'question.html', {
        'form': form,
        'answers': answers
    })

def unanswered_questions(request):
    unanswered_questions = UnansweredQuestion.objects.all()
    return render(request, 'unanswered_questions.html', {
        'unanswered_questions': unanswered_questions
    })

def add_answer_to_question(request, question_id):
    question = get_object_or_404(UnansweredQuestion, id=question_id)

    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            QuestionAnswer.objects.create(
                question=question.question,
                answer=answer
            )
            question.delete()  # Remove the unanswered question after answering
            return redirect('unanswered_questions')
    else:
        form = AddQuestionForm(initial={'question': question.question})

    return render(request, 'add_answer.html', {
        'form': form,
        'question': question
    })

def edit_unanswer_question(request, question_id):
    question = get_object_or_404(UnansweredQuestion, id=question_id)

    if request.method == 'POST':
        form = EditUnAnswerQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('unanswered_questions')
    else:
        form = EditUnAnswerQuestionForm(instance=question)

    return render(request, 'edit_question.html', {
        'form': form,
        'question': question
    })

def delete_unanswer_question(request, question_id):
    question = get_object_or_404(UnansweredQuestion, id=question_id)
    question.delete()
    return redirect('unanswered_questions')
