from django.db import models

class UploadFile(models.Model):
    question = models.TextField()
    answer = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()