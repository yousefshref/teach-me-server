# Generated by Django 4.2.5 on 2023-09-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
