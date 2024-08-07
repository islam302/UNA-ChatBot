from django import forms
from .models import QuestionAnswer

class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer
        fields = ['question', 'answer']

class QuestionForm(forms.Form):
    question = forms.CharField(label='Your question', max_length=255)

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Upload an Excel file')

