
from .models import Course
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def courses(request):

    c = Course.objects.all()

    return render(request,'courses.html',{'c':c})


def logout(request):
    auth.logout(request)
    return redirect('login')




