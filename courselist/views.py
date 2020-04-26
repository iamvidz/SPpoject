
from .models import Course
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def courses(request):
    c = Course.objects.all()

    return render(request,'courses.html',{'c':c})


def facultylogout(request):
    
	auth.logout(request)
	return redirect('facultylogin')


def studentlogout(request):
    
	auth.logout(request)
	return redirect('studentlogin')

@login_required
def add_courses(request): 

	if request.method == "POST": 
		form = CourseForm(request.POST,request.POST) 

		if form.is_valid(): 
			form.save()
             
			return redirect('courses') 
	else: 
		form = CourseForm() 
	return render(request, 'addcourses.html', {'form' : form }) 

def aboutus(request):

	return render(request,'aboutus.html')

def display(request):

	return redirect('display')