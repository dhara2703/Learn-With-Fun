from django.urls import path, re_path
from . import views

app_name = 'activity'

urlpatterns = [
    path('activities/', views.index, name = 'activities'),
    path('', views.subjects, name='subjects'),
    re_path(r'^subjects/(?P<subjectid>[\w-]+)$', views.topics, name='subjecttopics'),
    re_path(r'^topics/(?P<topicid>[\w-]+)$', views.subtopics, name='topicssubtopics'),
    re_path(r'^subtopic/(?P<subtopicid>[\w-]+)$',
            views.subtopic, name='subtopic'),
    re_path(r'^quiz/(?P<quizid>[\w-]+)$', views.quiz, name='quiz'),
    re_path(r'^result/(?P<studentresponse>[\w-]+)$', views.result, name='result'),

    path('report/', views.report, name='report'),

]


