from django.shortcuts import render
from .forms import student_form
from django.contrib.auth.models import User
# Create your views here.
from .forms import authenticationform
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout




def home(request):
    return render(request,'student/home.html',{'home':'active'})






def signup(request):
    if not request.user.is_authenticated:    
        if request.method == 'POST':
            form = student_form(request.POST)
            if form is not None:
                if form.is_valid():
                   name = form.cleaned_data['name']
                   stu_id = form.cleaned_data['stu_id']
                   email = form.cleaned_data['email']
                   password = form.cleaned_data['password']
                   user = User(username=stu_id, first_name=name, email=email)
                   user.set_password(password)
                   user.save()
            else:
                messages.warning(request,'Please Enter Your Information') 
                return redirect('/signup/')
        else:
            form = student_form()
        return render(request, 'student/signup.html', {'form': form,'signup':'active'})
    else:
        return redirect('/showbook/')
    









def stu_login(request): 
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=authenticationform(request=request,data=request.POST)
            if form != None:
                if form.is_valid():
                    username=form.cleaned_data['username']
                    password=form.cleaned_data['password']
                    user=authenticate(username=username,password=password)
    
                    if user is not None:
                        login(request,user)
                        messages.success(request,'login succesfully')
                        return redirect('/showbook/')
                    else:
                        messages.warning(request,'Please enter correct studend id and  password')
                        return redirect('/login/')
    
            else:
                messages.warning(request,'Please enter Student ID and Password')
                return redirect('/login/')
        else:
            form=authenticationform()
            return render(request,'student/login.html',{'form':form ,'login':'active'})
    else:
        return redirect('/showbook/')









def stu_logout(request):
    if request.user.is_authenticated:
       logout(request)
       messages.success(request,'Logout Successfully')
       return redirect('/login/')
    else:
        return redirect('/login/')




