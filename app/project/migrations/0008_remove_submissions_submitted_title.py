# Generated by Django 3.2.8 on 2021-10-15 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_submissions_submitted_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissions',
            name='submitted_title',
        ),
    ]