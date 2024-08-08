from django import forms
from .models import QuestionAnswer, UnansweredQuestion

class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Textarea(attrs={'class': 'form-control'}),
        }

class QuestionForm(forms.Form):
    question = forms.CharField(label='Your question', max_length=255)

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Upload an Excel file')

class UnansweredQuestionForm(forms.ModelForm):
    class Meta:
        model = UnansweredQuestion
        fields = ['question']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
        }


