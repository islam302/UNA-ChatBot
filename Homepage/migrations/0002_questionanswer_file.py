# Generated by Django 5.0.6 on 2024-05-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='file',
            field=models.FileField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]