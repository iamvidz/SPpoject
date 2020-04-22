from django.db import models

# Create your models here.

class Faculty(models.Model):

    name=models.CharField(max_length=50)
    facultyid=models.CharField(max_length=13)
    password=models.CharField(max_length=11)
    email=models.EmailField(max_length=254)
    