# Generated by Django 5.0.7 on 2024-08-09 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0003_questionanswer_funny_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='funny_answer',
        ),
    ]
