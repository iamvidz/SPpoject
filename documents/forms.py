from django import forms
from .models import Document

class DocsForm(forms.ModelForm):

    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Document
        fields=['document',]
