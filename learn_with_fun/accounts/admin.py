from django.contrib import admin
from .models import Country, Province, City, Student

class CountryAdmin(admin.ModelAdmin):
    list_display = ("c_country_id", "c_country_name", "c_country_isactive",)
    list_display_links = (
        "c_country_id", "c_country_name",)
    list_filter = ("c_country_isactive",)
    list_editable = ("c_country_isactive",)
    search_fields = ("c_country_name", "c_country_isactive",)
    list_per_page = 10


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("p_province_id", "p_province_name",
                    "p_province_country_id", "p_province_isactive",)
    list_display_links = ("p_province_id", "p_province_name",)
    list_filter = ("p_province_isactive", "p_province_country_id")
    list_editable = ("p_province_isactive", "p_province_country_id",)
    search_fields = ("p_province_country_id",
                     "p_province_name", "p_province_isactive",)
    list_per_page = 10


class CityAdmin(admin.ModelAdmin):
    list_display = ("c_city_id", "c_city_name",
                    "c_city_province_id", "c_city_isactive",)
    list_display_links = ("c_city_id", "c_city_name",)
    list_filter = ("c_city_province_id", "c_city_name", "c_city_isactive",)
    list_editable = ("c_city_isactive", "c_city_province_id",)
    search_fields = ("c_city_province_id",
                     "c_city_name", "c_city_isactive",)
    list_per_page = 10


class StudentAdmin(admin.ModelAdmin):
    list_display = ("s_student_id", "s_student_user_id",
                    "s_student_city", "s_student_province", "s_student_country", "s_student_isactive",)
    list_display_links = ("s_student_id", "s_student_user_id",
                          "s_student_city",)
    list_filter = ("s_student_city", "s_student_country", "s_student_province",
                   "s_student_isactive",)
    list_editable = ("s_student_country", "s_student_province","s_student_isactive",)
    search_fields = ("s_student_city", "s_student_country", "s_student_province",
                     "s_student_isactive",)
    list_per_page = 10


# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Student, StudentAdmin)
