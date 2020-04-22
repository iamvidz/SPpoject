
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
from courselist import urls

urlpatterns=[
    path("upload_document",views.upload_document,name='upload_document'),
    #path('download/', views.download_file),
    path('display',views.display_docs,name="display"),
    path('delete',views.delete,name="delete"),
    path("facultylogout",views.facultylogout,name='facultylogout'),
    path("studentlogout",views.studentlogout,name='studentlogout'),

    path('aboutus',views.aboutus),
    path('courses',views.courses),
]

if settings.DEBUG:

    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
