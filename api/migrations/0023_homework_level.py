# Generated by Django 4.2.5 on 2023-09-18 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_answeredquestion_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_homework', to='api.level'),
        ),
    ]