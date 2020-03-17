from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.utils.timezone import now




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
    s_account_created = models.DateField(default=datetime.date.today, auto_now=False, auto_now_add=False, verbose_name='student account creted on')
    s_account_updated_on = models.DateTimeField(default=now, verbose_name='student account updated on')
    
    def __str__(self):
        return self.s_student_user_id.first_name
  
