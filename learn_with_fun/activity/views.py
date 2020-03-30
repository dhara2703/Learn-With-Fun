from django.shortcuts import render, redirect
from .models import Subject, Grade, Topic, SubTopic, QuestionType, Quiz, Question, Answer
from django.contrib.auth.models import User
from django.apps import apps
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import json
import time
import datetime
import humanize
import pandas as pd
import requests
from django.template.defaulttags import register


Student = apps.get_model('accounts', 'Student')
StudentResponse = apps.get_model('accounts', 'StudentResponse')


# Create your views here.
def index(request):
    return render(request, 'activity/activities.html')


def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'activity/subjects.html', {'subjects': subjects})


def topics(request, subjectid):
    topics = Topic.objects.filter(t_topic_subject_id_id=subjectid)
    subject = Subject.objects.get(s_subject_id=subjectid)
    # print("Hello")
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
    start_time = time.time()
    stop_time = time.time()
    quiz = Quiz.objects.get(q_quiz_id=quizid)
    questions = Question.objects.filter(q_question_quiz_id=quizid)
    allanswers = []
    for question in questions:
        allanswers += Answer.objects.filter(
            a_answer_question_id=question.q_question_id)
    # allanswers = Answer.objects.all()
    subtopic = SubTopic.objects.get(st_subtopic_name=quiz.q_quiz_subtopic_id)
    topic = Topic.objects.get(t_topic_name=subtopic.st_subtopic_topic_id)
    subject = Subject.objects.get(s_subject_name=topic.t_topic_subject_id)
    user = User.objects.get(id=request.user.id)
    student = Student.objects.get(s_student_user_id=user.id)
    print(student.s_student_id)
    print(student)

    error_messages = ""

    # Checking the form is in POST
    if request.method == 'POST':
        counter = 0
        # loop through all questions to check all questions are answered
        for question in questions:
            # response = request.POST.get(question.getid)
            givenanswer = request.POST.get('response_' + question.getid())
            # if answer is not given, display an error message.
            if not givenanswer:
                counter += 1

        # moving the error messages to alert html for display javascript display
        if counter > 0:
            error_messages = 'Please Answer all Questions.'
            messages.error(request, error_messages)
            # print(counter)
        else:
            error_messages = ""
            # print(counter)

        # print(error_messages)
        if not error_messages:
            # questionResponse = {}
            total_score = 0
            responseArray = []
            student_answer = []
            for question in questions:
                questionid = Question.objects.get(
                    q_question_id=question.getid())
                givenanswer = request.POST.get('response_' + question.getid())
                # print(givenanswer)
                # print("Hello")
                # print(questionid)
                questionResponse = {
                    "questionid": questionid.getid(),
                    "answer": givenanswer}
                student_answer.append(request.POST.get(question.getid()))
                responseArray.append(questionResponse)
                # print(questionResponse)

                #### Store Student Responses as JSON format ####
                student_response_Json = json.dumps(responseArray)

                ###### Find Correct answer for the question #######
                correct_answer = 0
                correct_answer_text = ""
                answers = Answer.objects.filter(
                    a_answer_question_id=question.q_question_id)
                for answer in answers:
                    # print("The answer is " + str(answer.a_answer_text))
                    # print(answer.a_answer_iscorrect)
                    if answer.a_answer_iscorrect:
                        correct_answer = answer.getans()
                        correct_answer_text = answer.a_answer_text

                # print("/nFor Question " + str(questionid.getid()) + " Correct answer is  " + correct_answer_text)
                if correct_answer == givenanswer:
                    print("you are correct")
                    total_score += 1
                else:
                    print("Sorry, your answer is wrong")
            # print(total_score)
            # print("Total questions are: ")
            # print(questions.count())
            total_questions = questions.count()
            print("Total qus: " + str(total_questions))
            student_correct_answers = total_score
            student_score = float((total_score*100)/total_questions)

            ##### Store the Student Response to the Database ######
            student_response = StudentResponse()
            student_response.sr_studentresponse_student_id = student
            # print("-----------" + str(student_response.sr_studentresponse_student_id))
            student_response.sr_studentresponse_quiz_id = quiz
            # print("-----------" + str(student_response.sr_studentresponse_quiz_id))
            student_response.sr_studentresponse_que_ans = student_response_Json
            # print("-----------" + str(student_response.sr_studentresponse_que_ans))
            student_response.sr_studentresponse_score = "{0:.2f}".format(
                student_score)
            # print("-----------" + str(student_response.sr_studentresponse_score))
            student_response.save()
            
            print(json.dumps(responseArray))
            
            ############# Calculating Time taken for Quiz #################
            stop_time = time.time()
            # print(student_response)
            # print(student_response.sr_studentresponse_que_ans)
            
            ############# Converting the Response in Dataframe using Pandas #################
            data = pd.read_json(student_response.sr_studentresponse_que_ans)
            df = pd.DataFrame(data)
            print(df)
            time_elapsed = (stop_time - start_time) / 3600
            humanize.naturaldelta(datetime.timedelta(seconds=time_elapsed))
            print("total que: " + str(total_questions))
            print(student_response.sr_studentresponse_score)
            correct_answers = int(float(total_questions * (int(float(student_response.sr_studentresponse_score))))//100)
            print("aa " + str(correct_answers))
            wrong_answers = total_questions - correct_answers
            print(str(time_elapsed) + " seconds")
            return render(request, 'activity/result.html', {'student_response': student_response, 'quiz': quiz, 'questions': questions, 'answers': allanswers, 'subtopic': subtopic, 'topic': topic, 'subject': subject, "total_questions": total_questions, 'wrong_answers': wrong_answers, 'correct_answers': correct_answers})
            print("END")
    return render(request, 'activity/quiz.html', {'quiz': quiz, 'questions': questions, 'answers': allanswers, 'subtopic': subtopic, 'topic': topic, 'subject': subject})


def result(request, studentresponseid, total_questions, wrong_answers, correct_answers):
    print("here")
    student_response = StudentResponse.objects.get(
        sr_studentresponse_id=studentresponseid)
    quiz = Quiz.objects.get(
        q_quiz_id=student_response.sr_studentresponse_quiz_id)
    # questions = Question.objects.filter(q_question_quiz_id=quiz)
    # total_questions = questions.count()
    data = pd.read.json(student_response.sr_studentresponse_que_ans)
    df = pd.DataFrame(data)
    json_data = json.dumps(student_response.sr_studentresponse_que_ans)
    # wrong_answers = int(float(total_questions * (int(float(student_response.sr_studentresponse_score))))/100)
    # print("aa " + str(wrong_answers))
    # correct_answers = total_questions-wrong_answers
    subtopic = SubTopic.objects.get(st_subtopic_name=quiz.q_quiz_subtopic_id)
    topic = Topic.objects.get(t_topic_name=subtopic.st_subtopic_topic_id)
    subject = Subject.objects.get(s_subject_name=topic.t_topic_subject_id)
    user = User.objects.get(id=request.user.id)
    student = Student.objects.get(s_student_user_id=user.id)
    context = {
        'student_response': student_response,
        'quiz': quiz,
        'json_data': json_data,
        'subtopic': subtopic,
        'total_questions': total_questions,
        'wrong_answers': wrong_answers,
        'correct_answers': correct_answers,
        'topic': topic,
        'subject': subject,
    }
    print("HERE")
    details = json.loads(student_response.sr_studentresponse_que_ans)
    return render(request, 'activity/result.html', context)


def report(request):
    user = User.objects.get(id=request.user.id)
    student = Student.objects.get(s_student_user_id=user.id)
    student_responses = StudentResponse.objects.filter(
        sr_studentresponse_student_id=student)
    quiz = Quiz.objects.all()
    subtopic = SubTopic.objects.all()
    topic = Topic.objects.all()
    subject = Subject.objects.all()
    context = {
        'student_responses': student_responses, 
        'student': student,
        'quiz': quiz,
        'subtopic': subtopic,
        'topic': topic,
        'subject': subject,
    }
    return render(request, 'activity/report.html', context)
