# Generated by Django 3.2.8 on 2021-11-10 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_alter_submissions_submission_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='assignment_status',
            field=models.BooleanField(default=False),
        ),
    ]