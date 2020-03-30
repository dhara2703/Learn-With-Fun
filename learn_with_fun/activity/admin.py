from django.contrib import admin
from .models import Subject, Grade, Topic, SubTopic, QuestionType, Quiz, Question, Answer
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("s_subject_id", "s_subject_name",
                    "s_subject_desc", "s_subject_image", "s_subject_isactive",
                    "s_subject_created_on", "s_subject_updated_on",)
    list_display_links = ("s_subject_name",)
    list_filter = ("s_subject_isactive",)
    list_editable = ("s_subject_isactive",)
    search_fields = ("s_subject_name",)
    list_per_page = 10


class GradeAdmin(admin.ModelAdmin):
    list_display = ("g_grade_id", "g_grade_name",
                    "g_grade_isactive", "g_grade_created_on", "g_grade_updated_on",)
    list_display_links = ("g_grade_name",)
    list_filter = ("g_grade_isactive",)
    list_editable = ("g_grade_isactive",)
    search_fields = ("g_grade_name",)
    list_per_page = 10


class TopicAdmin(admin.ModelAdmin):
    list_display = ("t_topic_id", "t_topic_name",
                    "t_topic_desc", "t_topic_subject_id", "t_topic_isactive",)
    list_display_links = ("t_topic_name",)
    list_filter = ("t_topic_isactive",)
    list_editable = ("t_topic_isactive",)
    search_fields = ("t_topic_name",)
    list_per_page = 10


class SubTopicAdmin(admin.ModelAdmin):
    list_display = ("st_subtopic_id", "st_subtopic_name",
                    "st_subtopic_desc", "st_subtopic_grade_id", "st_subtopic_topic_id", "st_subtopic_isactive",)
    list_display_links = ("st_subtopic_name",)
    list_filter = ("st_subtopic_isactive",)
    list_editable = ("st_subtopic_isactive",)
    search_fields = ("st_subtopic_name",)
    list_per_page = 10


class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ("qt_questiontype_id", "qt_questiontype_name",
                    "qt_questiontype_isactive",)
    list_display_links = ("qt_questiontype_name",)
    list_filter = ("qt_questiontype_isactive",)
    list_editable = ("qt_questiontype_isactive",)
    search_fields = ("qt_questiontype_name",)
    list_per_page = 10


class QuizAdmin(admin.ModelAdmin):
    list_display = ("q_quiz_id", "q_quiz_subtopic_id",
                    "q_quiz_name", "q_quiz_isactive",)
    list_display_links = ("q_quiz_name",)
    list_filter = ("q_quiz_isactive",)
    list_editable = ("q_quiz_isactive",)
    search_fields = ("q_quiz_name",)
    list_per_page = 10


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("q_question_id", "q_question_text",  "q_question_quiz_id", 
                    "q_question_questiontype_id",                   
                    "q_question_hint", "q_question_isactive",)
    list_display_links = ("q_question_text",)
    list_filter = ("q_question_isactive", "q_question_quiz_id",
                   "q_question_questiontype_id",)
    list_editable = ("q_question_isactive",
                     "q_question_questiontype_id", "q_question_quiz_id")
    search_fields = ("q_question_text",)
    list_per_page = 10


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("a_answer_id", "a_answer_text",  "a_answer_question_id",
                    "a_answer_iscorrect",
                    "a_answer_isactive",)
    list_display_links = ("a_answer_text",)
    list_filter = ("a_answer_question_id", "a_answer_iscorrect",
                   "a_answer_isactive",)
    list_editable = ("a_answer_iscorrect",
                     "a_answer_isactive",)
    search_fields = ("a_answer_text",)
    list_per_page = 10


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(SubTopic, SubTopicAdmin)
admin.site.register(QuestionType, QuestionTypeAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
