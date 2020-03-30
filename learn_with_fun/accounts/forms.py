from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Country, Province, City, Student
from django.contrib.auth.models import User
from django.apps import apps

# Student Sign Up Form

class UserAccountCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'password1', 'password2')

    def save(self, commit=True):
        user = super(UserAccountCreationForm, self).save(commit=False)
        user.is_staff = False
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user
    
    # def clean(self):
    #     cleaned_data = super(UserAccountCreationForm, self).clean()
    #     username = cleaned_data.get('username')
    #     email = cleaned_data.get('email')
    #     first_name = cleaned_data.get('first_name')
    #     last_name = cleaned_data.get('last_name')
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
    #     if not username and not email and not first_name and not last_name and not password1 and not password2:
    #         raise forms.ValidationError('You have to write something!')


class UserAccountUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'size': '40'}))
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'size': '40'}))
    last_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'size': '40'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class StudentCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('s_student_city', 's_student_province',
                  's_student_country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['s_student_city'].initial = City.objects.first()
        self.fields['s_student_province'].initial = Province.objects.first()
        self.fields['s_student_country'].initial = Country.objects.first()


class StudentChangeForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('s_student_city', 's_student_province',
                  's_student_country')
    
  
