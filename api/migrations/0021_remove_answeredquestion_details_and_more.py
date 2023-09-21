# Generated by Django 4.2.5 on 2023-09-18 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_answeredquestion_homework_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answeredquestion',
            name='details',
        ),
        migrations.AddField(
            model_name='answeredquestion',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_answered', to='api.student'),
        ),
        migrations.AlterField(
            model_name='answeredquestion',
            name='homework',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_answered', to='api.homework'),
        ),
        migrations.DeleteModel(
            name='AnswerdQuestionDetails',
        ),
    ]
