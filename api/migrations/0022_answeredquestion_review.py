# Generated by Django 4.2.5 on 2023-09-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_answeredquestion_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeredquestion',
            name='review',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
