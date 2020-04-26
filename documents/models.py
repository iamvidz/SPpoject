from django.db import models
#from courselist.models import *

# Create your models here.

class Document(models.Model):

    #course = models.ForeignKey(Course, on_delete=models.CASCADE)
    document = models.FileField()
    date = models.DateTimeField(auto_now=True)
    

    