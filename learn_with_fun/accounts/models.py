from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.utils.timezone import now
from jsonfield import JSONField

# Create your models here.


class Country(models.Model):
    class Meta:
        db_table = 'tblkpCountry'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        
    c_country_id = models.AutoField(primary_key=True, verbose_name='country id')
    c_country_name = models.CharField(unique=True, max_length=90, verbose_name='country name')
    c_country_isactive = models.BooleanField(default=True, verbose_name= 'is country active')
    
    def __str__(self):
        return self.c_country_name
    

class Province(models.Model):
    class Meta:
        db_table = 'tblkpProvince'
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
        unique_together = ('p_province_name', 'p_province_country_id')
        
    p_province_id = models.AutoField(primary_key=True, verbose_name= 'province id')
    p_province_name = models.CharField(max_length=90, verbose_name='province/State name')
    p_province_country_id = models.ForeignKey(
        'Country', on_delete=models.PROTECT, verbose_name='country name')
    p_province_isactive = models.BooleanField(default=True, verbose_name= 'is province active')
    
    def __str__(self):
        return self.p_province_name
    
    
class City(models.Model):
    class Meta:
        db_table = 'tblkpCity'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        unique_together = ('c_city_name', 'c_city_province_id')
        
    c_city_id = models.AutoField(primary_key=True, verbose_name= 'city id')
    c_city_name = models.CharField(max_length=190, verbose_name='city name')
    c_city_province_id = models.ForeignKey(
        'Province', on_delete=models.PROTECT, verbose_name='province id')
    c_city_isactive = models.BooleanField(default=True, verbose_name= 'is city active')
    
    def __str__(self):
        return self.c_city_name


class Student(models.Model):
    class Meta:
        db_table = 'tblStudent'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        
    s_student_id = models.AutoField(primary_key=True, verbose_name='student id')
    s_student_user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='student user id')
    s_student_city = models.ForeignKey('City', blank=True, null=True, on_delete=models.PROTECT, verbose_name='student city')
    s_student_province = models.ForeignKey('Province', blank=True, null=True, on_delete=models.PROTECT, verbose_name='student province')
    s_student_country = models.ForeignKey(
        'Country', blank=True, null=True, on_delete=models.PROTECT, verbose_name='student country')
    s_student_isactive = models.BooleanField(default=True, verbose_name= 'is student active')
    s_account_created = models.DateField(default=datetime.date.today, auto_now=False, auto_now_add=False, verbose_name='student account created on')
    s_account_updated_on = models.DateTimeField(default=now, verbose_name='student account updated on')
    
    def __str__(self):
        return self.s_student_user_id.first_name

    def getId(self):return str(self.s_student_id)

  

class StudentResponse(models.Model):
    class Meta:
        db_table = 'tblStudentResponse'
        verbose_name = 'Student Response'
        verbose_name_plural = 'Student Responses'

    sr_studentresponse_id = models.AutoField(primary_key=True, verbose_name='student response id')
    sr_studentresponse_student_id = models.ForeignKey('Student', on_delete=models.PROTECT, verbose_name='student')
    sr_studentresponse_quiz_id = models.ForeignKey('activity.Quiz', default=1, on_delete=models.PROTECT, verbose_name='Quiz')
    sr_studentresponse_que_ans = JSONField(max_length=1000, null=True, verbose_name='Student Response Question And Answer')
    sr_studentresponse_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, verbose_name='student answer score')
    sr_studentresponse_created_on = models.DateTimeField(auto_now_add= True, verbose_name='student response created on')

    def __str__(self):
        return str(self.sr_studentresponse_id)


    def save(self, *args, **kwargs):
        self.sr_studentresponse_created_on = timezone.now()
        return super(StudentResponse, self).save(*args, **kwargs)

    def getanswer(self):
        responsejson = self.sr_studentresponse_que_ans
        response = json.loads(responsejson)

        answer = []
        
        for answer in response:
            answer.append(answer["answer"])
        
        return answer

    def getquestionid(self):
        responsejson = self.sr_studentresponse_que_ans
        response = json.loads(responsejson)

        questionid = []

        for question in response:
            questionid.append(question["questionid"])

        return questionid

