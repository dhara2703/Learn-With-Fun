from django.shortcuts import render
from .models import Subject, Grade, Topic, SubTopic, QuestionType, Quiz, Question, Answer
from django.apps import apps
from django.contrib import messages
import datetime

Student = apps.get_model('accounts', 'Student')
StudentResponse = apps.get_model('accounts', 'StudentResponse')


# Create your views here.
def index(request):
    return render(request, 'activity/activities.html')


def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'activity/subjects.html', {'subjects':subjects})


def topics(request, subjectid):
    topics = Topic.objects.filter(t_topic_subject_id_id=subjectid)
    subject = Subject.objects.get(s_subject_id=subjectid)
    print("Hello")
    print(topics)
    return render(request, 'activity/topics.html', {'topics': topics, 'subject': subject})

def subtopics(request, topicid):
    subtopics = SubTopic.objects.filter(st_subtopic_topic_id=topicid)
    topic = Topic.objects.get(t_topic_id=topicid)
    subject = Subject.objects.get(s_subject_name=topic.t_topic_subject_id)
    print(subtopics)
    print(topic)
    print(subject)
    return render(request, 'activity/subtopics.html', {'subtopics': subtopics, 'topic': topic, 'subject': subject})


def subtopic(request, subtopicid):
    subtopic = SubTopic.objects.get(st_subtopic_id=subtopicid)
    quizzes = Quiz.objects.filter(q_quiz_subtopic_id=subtopicid)
    print(subtopic)
    print(quizzes)
    topic = Topic.objects.get(t_topic_name=subtopic.st_subtopic_topic_id)
    print(topic)
    subject = Subject.objects.get(s_subject_name=topic.t_topic_subject_id)
    print(subject)
    return render(request, 'activity/subtopic.html', {'subtopic': subtopic, 'quizzes': quizzes, 'topic': topic, 'subject': subject})


def quiz(request, quizid):
    quiz = Quiz.objects.get(q_quiz_id=quizid)
    questions = Question.objects.filter(q_question_quiz_id=quizid)
    allanswers = []
    for question in questions:
        allanswers += Answer.objects.filter(a_answer_question_id=question.q_question_id)
    # allanswers = Answer.objects.all()
    subtopic = SubTopic.objects.get(st_subtopic_name=quiz.q_quiz_subtopic_id)
    topic = Topic.objects.get(t_topic_name=subtopic.st_subtopic_topic_id)
    subject = Subject.objects.get(s_subject_name=topic.t_topic_subject_id)
    student = Student.objects.get(s_student_user_id=request.user.id)
    print(student)

    if request.method == 'POST':
        print(request)
        for question in questions:
            responseArray = []
            student_answer = []
            questionid = Question.objects.get(q_question_id= question.getid())
            a = request.POST.get('response_' + question.getid())
            print(a)
            print("Hello")
            print(questionid)
            questionResponse = {
                "questionid":questionid.getid(),
                "answer":a}
            student_answer.append(request.POST.get(question.getid()))
            responseArray.append(questionResponse)
            print("hello")
            print(responseArray)

    return render(request, 'activity/quiz.html', {'quiz': quiz, 'questions': questions, 'answers': allanswers, 'subtopic': subtopic, 'topic': topic, 'subject': subject})
