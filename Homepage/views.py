from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import openai

from .models import QuestionAnswer


@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')

        try:
            qa = QuestionAnswer.objects.get(question__icontains=user_message)
            # Replace this with your logic to process the answer
            response_text = qa.answer
        except ObjectDoesNotExist:
            # Handle case where no answer is found
            response_text = "Sorry, I couldn't find an answer to your question."

        return JsonResponse({'response': response_text})

    return render(request, 'chatbot.html')
