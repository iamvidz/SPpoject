
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path("courses",views.courses,name='courses'),
    
    path("logout",views.logout,name='logout'),
   
]