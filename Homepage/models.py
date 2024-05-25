from django.db import models


class QuestionAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
