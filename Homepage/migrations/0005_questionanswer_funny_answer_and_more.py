# Generated by Django 4.2.9 on 2024-08-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0004_remove_questionanswer_funny_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='funny_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='unansweredquestion',
            name='funny_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
