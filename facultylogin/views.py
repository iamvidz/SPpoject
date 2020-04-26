from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.

def login(request):

    if request.method == 'POST':
        facultyid = request.POST['facultyid']
        password = request.POST['password']

        user = auth.authenticate(username=facultyid,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('courses')
        else:
            messages.info(request,'invalid username or password')
            return redirect('facultylogin')
            
    else:
        return render(request,'faculty.html')


def register(request):


    if request.method == 'POST':
        fname=request.POST['fname']
        facultyid = request.POST['facultyid']
        password = request.POST['password']
        repass = request.POST['repass']
        email = request.POST['email']

        if password == repass :
            if User.objects.filter(username=facultyid).exists():
                messages.info(request,'User already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=facultyid,password=password,email=email,first_name=fname,is_staff=True)
                user.save()
                print('user created')
                return redirect('facultylogin')
        else:
            messages.info(request,"password does not match")
            return redirect('register')
       

    else :
        return render(request,'facultyregister.html')


def logout(request):
    auth.logout(request)
    return redirect('facultylogin')