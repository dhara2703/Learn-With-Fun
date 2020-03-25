from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, City, Province, Country
from django.contrib.auth.models import User
from datetime import datetime
from django.apps import apps
from .import forms



# Login View
def accounts_login(request):
    # If user is already logged in then redirect to the main page
    if request.user.is_authenticated:
        return redirect('activity:activities')
    
    # If user is not logged in
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            
            # If user requested some specific page then redirect to that page
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('activity:subjects')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form':form})

            
# Logout View
@login_required(login_url="/accounts/login/")
def accounts_logout(request):
	if request.method == 'POST':
		logout(request)
		messages.info(request, "Logged out successfully!")
		return redirect('accounts:accountLogin')
	if request.method == 'GET':
		logout(request)
		messages.info(request, "Logged out successfully!")
		return redirect('accounts:accountLogin')

# Sign Up Form
def account_create(request):
	if request.method == 'POST':
         userform = forms.UserAccountCreationForm(request.POST)
         studentform = forms.StudentCreationForm(request.POST)
        #  messages.error(request, "Testing")
         if (userform.is_valid() and studentform.is_valid()):
             user = userform.save()
             student = studentform.save(commit=False)
             student.s_student_user_id = user
             student.save()
             messages.info(request, "Thanks for registering. You are now logged in.")
             user = authenticate(
			    username=userform.cleaned_data['username'], password=userform.cleaned_data['password1'],)
             login(request, user)
             return redirect('activity:subjects')
	else:
		userform = forms.UserAccountCreationForm()
		studentform = forms.StudentCreationForm()

	return render(request, 'accounts/account_create.html', {'userform': userform, 'studentform': studentform})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@login_required
def user_profile(request):
    # currentuser = request.id
    # print(currentuser)
    # print("Hello")
    # currentuser = request.user
    # print(request.user)
    # if Student.objects.get(s_student_user_id=currentuser.id):
    #     studentinfo = studentinfo = Student.objects.get(s_student_user_id=currentuser.id)
    #     print(studentinfo.s_student_province)
    #     return render(request, 'accounts/user_profile.html', {'currentuser': currentuser, 'studentinfo':studentinfo})
    # else:
    #     message = "There is no profile exist."
    #     return render(request, 'accounts/user_profile.html', {'currentuser': currentuser, 'message': message})
    user = User.objects.get(id=request.user.id)
    print(user.username)
    try:
        student = Student.objects.get(s_student_user_id=user.id)
        print(student.s_student_id)
    except:
        return render(request, 'accounts/user_profile.html', {'user':user})
    return render(request, 'accounts/user_profile.html', {'user':user, 'student':student})


@login_required(login_url="/accounts/login/")
def user_profile_update(request):
    user = User.objects.get(id=request.user.id)
    print(user.username)
    try:
        student = Student.objects.get(s_student_user_id=user.id)
        print(student.s_student_id)
        if request.method == 'POST':
            userform = forms.UserAccountUpdateForm(
                request.POST or None, instance=user)
            studentform = forms.StudentChangeForm(
                request.POST or None, instance=student)
            if (userform.is_valid() and studentform.is_valid()):
                userform.save()
                studentform.save()
                messages.info(
                    request, "Your Student Profile is Successfully Updated")
                return redirect('accounts:myprofile')
        else:
            data = {
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                    }
            data1 = {
                        'student_city': student.s_student_city,
                        's_student_province': student.s_student_province,
                        's_student_country': student.s_student_country, 
                    }
            userform = forms.UserAccountUpdateForm(initial=data)
            studentform = forms.StudentChangeForm(initial=data1)
        return render(request, 'accounts/account_create.html', {'userform': userform, 'studentform': studentform})
    except:
        print(user.username)
        if request.method == 'POST':
            userform = forms.UserAccountUpdateForm(
                request.POST or None, instance=user)
            if (userform.is_valid()):
                userform.save()
                messages.info(
                    request, "Your User Profile is Successfully Updated.")
                return redirect('accounts:myprofile')
        else:
            data = {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
            userform = forms.UserAccountUpdateForm()
        return render(request, 'accounts/account_create.html', {'userform': userform})
