from django import forms
from .models import Question, QuestionType, Answer, SubTopic, Topic, Quiz 
from django.contrib.auth.models import User
from django.apps import apps

Student = apps.get_model('accounts', 'Student')
StudentResponse = apps.get_model('accounts', 'StudentResponse')

DISPLAY_CHOICES = (
    ("locationbox", "Display Location"),
    ("displaybox", "Display Direction")
)


class MyForm(forms.Form):
    display_type = forms.ChoiceField(
        widget=forms.RadioSelect, choices=DISPLAY_CHOICES)
