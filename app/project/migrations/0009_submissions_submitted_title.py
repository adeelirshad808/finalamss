# Generated by Django 3.2.8 on 2021-10-15 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_remove_submissions_submitted_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='submitted_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.assignment'),
        ),
    ]