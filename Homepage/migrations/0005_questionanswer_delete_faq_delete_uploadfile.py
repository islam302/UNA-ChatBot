# Generated by Django 5.0.6 on 2024-05-28 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0004_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FAQ',
        ),
        migrations.DeleteModel(
            name='UploadFile',
        ),
    ]