from django import forms 
from .models import ConvertImage 

class ImageForm(forms.ModelForm):
    class Meta:
        model = ConvertImage
        fields = ['originalImage']