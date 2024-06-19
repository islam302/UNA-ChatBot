from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


class QuestionForm(forms.Form):
    question = forms.CharField(label='Your question', max_length=255)
