# Generated by Django 5.0.6 on 2024-05-29 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0007_alter_questionanswer_created_at'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='questionanswer',
            table='homepage_questionanswer',
        ),
    ]
