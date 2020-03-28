	from django import forms
from .models import Question, QuestionType, Answer, SubTopic, Topic, Quiz 
from django.contrib.auth.models import User
from django.apps import apps

Student = apps.get_model('accounts', 'Student')
StudentResponse = apps.get_model('accounts', 'StudentResponse')
