from django.db import models
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.

class Subject(models.Model):
    class Meta:
        db_table = 'tblSubject'
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        
    s_subject_id = models.AutoField(primary_key=True, verbose_name='subject id')
    s_subject_name = models.CharField(
        unique=True, max_length=50, verbose_name='subject name')
    s_subject_desc = models.TextField(verbose_name='subject description', blank=True, null=True)
    s_subject_image = models.ImageField(default='background.png', blank=True, verbose_name='subject image')
    s_subject_isactive = models.BooleanField(default=True, verbose_name= 'is subject active')
    s_subject_created_on = models.DateTimeField(
        default=now, editable=False, verbose_name='subject created on')
    s_subject_updated_on = models.DateTimeField(
        default=now, verbose_name='subject updated on')
    
    def __str__(self):
        return self.s_subject_name
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.s_subject_id:
            self.s_subject_created_on = timezone.now()
        self.s_subject_updated_on = timezone.now()
        return super(Subject, self).save(*args, **kwargs)
    

class Grade(models.Model):
    class Meta:
        db_table = 'tblGrade'
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        
    g_grade_id = models.AutoField(primary_key=True, verbose_name='grade id')
    g_grade_name = models.CharField(
        unique=True, max_length=50, verbose_name='grade name')
    g_grade_isactive = models.BooleanField(default=True, verbose_name= 'is grade active')
    g_grade_created_on = models.DateTimeField(
        default=now, editable=False, verbose_name='grade created on')
    g_grade_updated_on = models.DateTimeField(
        default=now, verbose_name='grade updated on')
    
    def __str__(self):
        return self.g_grade_name
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.g_grade_id:
            self.g_grade_created_on = timezone.now()
        self.g_grade_updated_on = timezone.now()
        return super(Grade, self).save(*args, **kwargs)
    
    
class Topic(models.Model):
    class Meta:
        db_table = 'tblTopic'
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        unique_together = ('t_topic_name', 't_topic_subject_id')
        
    t_topic_id = models.AutoField(primary_key=True, verbose_name='topic id')
    t_topic_name = models.CharField(
        unique=True, max_length=50, verbose_name='topic name')
    t_topic_desc = models.TextField(verbose_name='topic description', blank=True, null=True)
    t_topic_subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE, verbose_name='topic subject id')
    t_topic_isactive = models.BooleanField(default=True, verbose_name= 'is topic active')
    
    def __str__(self):
        return self.t_topic_name
    
class SubTopic(models.Model):
    class Meta:
        db_table = 'tblSubTopic'
        verbose_name = 'SubTopic'
        verbose_name_plural = 'SubTopics'
        unique_together = (
            'st_subtopic_name', 'st_subtopic_grade_id', 'st_subtopic_topic_id')

    st_subtopic_id = models.AutoField(primary_key=True, verbose_name='subtopic id')
    st_subtopic_name = models.CharField(max_length=50, verbose_name='subtopic name')
    st_subtopic_desc = models.TextField(verbose_name='subtopic description', blank=True, null=True)
    st_subtopic_grade_id = models.ForeignKey('Grade', on_delete=models.CASCADE, verbose_name='topic grade id')
    st_subtopic_topic_id = models.ForeignKey('Topic', on_delete=models.CASCADE, verbose_name='subtopic topic id')
    st_subtopic_isactive = models.BooleanField(default=True, verbose_name='is subtopic active')

    def __str__(self):
        return str(self.st_subtopic_name)


class QuestionType(models.Model):
    class Meta:
        db_table = 'lkpQuestionType'
        verbose_name = 'QuestionType'
        verbose_name_plural = 'QuestionTypes'

    qt_questiontype_id = models.AutoField(
        primary_key=True, verbose_name='questiontype id')
    qt_questiontype_name = models.CharField(
        unique=True, max_length=100, verbose_name='questiontype name')
    qt_questiontype_isactive = models.BooleanField(
        default=True, verbose_name='is questiontype active')

    def __str__(self):
        return self.qt_questiontype_name


class Quiz(models.Model):
    class Meta:
        db_table = 'tblQuiz'
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        unique_together = (
            'q_quiz_subtopic_id', 'q_quiz_name')

    q_quiz_id = models.AutoField(
        primary_key=True, verbose_name='quiz id')
    q_quiz_subtopic_id = models.ForeignKey(
        'SubTopic', on_delete=models.PROTECT, verbose_name='quiz subtopic')
    q_quiz_name = models.CharField(unique=True, max_length=100, verbose_name='quiz name')
    q_quiz_isactive = models.BooleanField(
        default=True, verbose_name='is quiz active')

    def __str__(self):
        return self.q_quiz_name


class Question(models.Model):
    class Meta:
        db_table = 'tblQuestion'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        unique_together = (
            'q_question_questiontype_id', 'q_question_quiz_id', 'q_question_text')

    q_question_id = models.AutoField(
        primary_key=True, verbose_name='question id')
    q_question_questiontype_id = models.ForeignKey(
        'QuestionType', on_delete=models.PROTECT, verbose_name='question type')
    q_question_quiz_id = models.ForeignKey(
        'Quiz', on_delete=models.PROTECT, verbose_name='question quiz id')
    q_question_text = models.CharField(
        unique=True, max_length=250, verbose_name='question text')
    q_question_hint = models.TextField(default = "Hint is Not Provided", max_length=250, verbose_name='question hint')
    q_question_isactive = models.BooleanField(
        default=True, verbose_name='is question active')

    def __str__(self):
        return self.q_question_text


class Answer(models.Model):
    class Meta:
        db_table = 'tblAnswer'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        unique_together = (
            'a_answer_question_id', 'a_answer_text')

    a_answer_id = models.AutoField(
        primary_key=True, verbose_name='answer id')
    a_answer_question_id = models.ForeignKey(
        'Question', on_delete=models.PROTECT, verbose_name='question')
    a_answer_text = models.CharField(max_length=250, verbose_name='answer text')
    a_answer_iscorrect = models.BooleanField(default=False, verbose_name='is correct answer')
    a_answer_isactive = models.BooleanField(default=True, verbose_name='is answer active')

    def __str__(self):
        return self.a_answer_text
