from django.shortcuts import render
from .models import Subject, Grade, Topic, SubTopic, QuestionType, Quiz, Question, Answer

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
    print(quiz)
    questions = Question.objects.filter(q_question_quiz_id=quizid)
    print(questions)
    allanswers = Answer.objects.all()
    print(questions)
    subtopic = SubTopic.objects.get(st_subtopic_name=quiz.q_quiz_subtopic_id)
    print(subtopic)
    topic = Topic.objects.get(t_topic_name=subtopic.st_subtopic_topic_id)
    print(topic)
    subject = Subject.objects.get(s_subject_name=topic.t_topic_subject_id)
    print(subject)
    
    return render(request, 'activity/quiz.html', {'quiz': quiz, 'questions': questions, 'answers': allanswers, 'subtopic': subtopic, 'topic': topic, 'subject': subject})
