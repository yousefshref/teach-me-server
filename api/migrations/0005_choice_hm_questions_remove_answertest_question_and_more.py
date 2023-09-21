# Generated by Django 4.2.5 on 2023-09-18 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_media_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(blank=True, max_length=500, null=True)),
                ('is_correct', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('question', models.CharField(blank=True, max_length=500, null=True)),
                ('hm', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.hm')),
            ],
        ),
        migrations.RemoveField(
            model_name='answertest',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answertest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='level',
        ),
        migrations.RemoveField(
            model_name='homeworkanswer',
            name='homework',
        ),
        migrations.RemoveField(
            model_name='homeworkanswer',
            name='level',
        ),
        migrations.RemoveField(
            model_name='homeworkanswer',
            name='student',
        ),
        migrations.RemoveField(
            model_name='homeworkwronganswers',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='homeworkwronganswers',
            name='homework_answers',
        ),
        migrations.RemoveField(
            model_name='homeworkwronganswers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='media',
            name='level',
        ),
        migrations.RemoveField(
            model_name='question',
            name='homework',
        ),
        migrations.RemoveField(
            model_name='questiontest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='test',
            name='level',
        ),
        migrations.RemoveField(
            model_name='testanswer',
            name='level',
        ),
        migrations.RemoveField(
            model_name='testanswer',
            name='student',
        ),
        migrations.RemoveField(
            model_name='testanswer',
            name='test',
        ),
        migrations.RemoveField(
            model_name='testwronganswers',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='testwronganswers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='testwronganswers',
            name='test_answers',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='AnswerTest',
        ),
        migrations.DeleteModel(
            name='Homework',
        ),
        migrations.DeleteModel(
            name='HomeworkAnswer',
        ),
        migrations.DeleteModel(
            name='HomeworkWrongAnswers',
        ),
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionTest',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='TestAnswer',
        ),
        migrations.DeleteModel(
            name='TestWrongAnswers',
        ),
        migrations.AddField(
            model_name='choice',
            name='hm',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.hm'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.questions'),
        ),
    ]
