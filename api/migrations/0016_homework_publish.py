# Generated by Django 4.2.5 on 2023-09-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_answer_homework_question_homework'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]