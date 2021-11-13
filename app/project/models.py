from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse


class Teacher(models.Model):
    teacher_username = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="assignments")
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


class Assignment(models.Model):
    assignment_creator = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="assignments")
    assignment_title = models.CharField(max_length=30)
    assignment_details = models.TextField()
    assignment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.assignment_title)

# This holds all the grading and stuff for a submission of an assignment


class Submissions(models.Model):
    submitted_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_file = models.FileField(null=False, blank=True, default='')
    submitted_to = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True)
    submission_title = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, null=True, blank=True)
    submission_status = models.BooleanField(default=False)
    marks_obtained = models.FloatField(null=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_by']

    def __str__(self):
        return str(self.submitted_by)

    def get_absolute_url(self):
        # return reverse('article_detail', args=str((self.id)))
        return reverse('index')
