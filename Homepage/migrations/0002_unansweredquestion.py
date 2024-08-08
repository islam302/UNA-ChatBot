# Generated by Django 5.0.7 on 2024-08-08 09:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnansweredQuestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
