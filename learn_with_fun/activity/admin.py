from django.contrib import admin
from .models import Subject, Grade, Topic, SubTopic, QuestionType, Quiz, Question, Answer
# Register your models here.

admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(QuestionType)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)


