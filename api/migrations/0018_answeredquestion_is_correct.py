# Generated by Django 4.2.5 on 2023-09-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_answeredquestion_homework'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeredquestion',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
