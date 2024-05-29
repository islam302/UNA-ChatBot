# Generated by Django 5.0.6 on 2024-05-28 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0002_questionanswer_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
    ]