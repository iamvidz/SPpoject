from django.db import models

# Create your models here.

class Document(models.Model):

    document = models.FileField()
    
    def extension(self):
        extension = os.path.splitext(self.document.name)
        return extension
    