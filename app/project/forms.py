from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import Submissions


class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class assignmentUploadForm(ModelForm):
    class Meta:
        model = Submissions
        fields = ('submitted_by', 'submitted_to',
                  'submission_title', 'submission_file', 'submission_status')

        widgets = {
            'submitted_by': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', }),
            'submitted_to': forms.Select(attrs={'class': 'form-control'}),
            'submission_title': forms.Select(attrs={'class': 'form-control'}),
        }
