
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path("courses",views.courses,name='courses'),
    
    path("facultylogout",views.facultylogout,name='facultylogout'),
    path("studentlogout",views.studentlogout,name='studentlogout'),

    #path("addcourses",views.addcourses,name='addcourses'),
    path("add_courses",views.add_courses,name='add_courses'),
    path("aboutus",views.aboutus),
    path("display",views.display),
]