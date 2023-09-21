# Generated by Django 4.2.5 on 2023-09-19 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_answeredquestion_correct_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('file', models.FileField(blank=True, null=True, upload_to='pdf/')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_lesson', to='api.level')),
            ],
        ),
    ]
