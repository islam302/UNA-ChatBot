# Generated by Django 5.0.6 on 2024-07-07 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='created_at',
        ),
    ]