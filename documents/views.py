

# Create your views here.
from django.shortcuts import render,redirect
from .forms import DocsForm
from .models import Document

import mimetypes
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from courselist import views
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404 


@login_required(login_url="facultylogin")
def upload_document(request):
 
    if request.method == 'POST':
        form = DocsForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return redirect('display')
    else:
        form = DocsForm()

    return render(request, 'documents.html', {'form': form})


def delete(request):
    
    if request.method=="POST":
        doc=request.POST['pk']
        b=Document.objects.get(id=doc).delete()
    #b = Document.objects.get(id)

    #Entry.objects.filter(document=b).delete()

    return redirect('display')


@login_required
def display_docs(request):


    #docs = Document.objects.all()
    docs = Document.objects.filter(date__lte=timezone.now()).order_by('-date')

    return render(request, 'documents.html', {'docs' : docs})



def download_file(request):

    pass



def aboutus(request):

    return render(request,'aboutus.html')



def facultylogout(request):
    
	auth.logout(request)
	return redirect('facultylogin')


def studentlogout(request):
    
	auth.logout(request)
	return redirect('studentlogin')


def courses(request):
   return redirect('courses')