from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.base import Model


class Teacher(models.Model):
    teacher_username = models.OneToOneField(User, on_delete=models.CASCADE)
    t_full_name = models.CharField(max_length=20)
    is_Teacher = models.BooleanField(default=True)

    def __str__(self):
        return str(self.teacher_username)


class Student(models.Model):
    student_username = models.OneToOneField(User,
                                            on_delete=models.CASCADE,
                                            null=True)
    s_full_name = models.CharField(max_length=20)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return str(self.student_username)


# This holds all the grading and stuff for a submission of an assignment
class Submissions(models.Model):
    submitted_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_file = models.FileField(null=False)

    def __str__(self):
        return str(self.submitted_by)


class Assignment(models.Model):
    assignment_creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assignment_title = models.CharField(max_length=30)
    assignment_details = models.TextField()
    assignment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.assignment_creator)
