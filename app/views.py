from django.shortcuts import render
from django.http import HttpResponse
from wand.image import Image
import tempfile
import os
from .models import ConvertImage
from django import forms 
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')


class ConvertImageForm(forms.ModelForm):
    class Meta:
        model = ConvertImage
        fields = ['originalImage', 'convertedImage']

def upload_image(request):
    if request.method == 'POST':
        form = ConvertImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form, 'message': 'Image uploaded successfully.'})
    else:
        form = ConvertImageForm()

    return render(request, 'index.html', {'form': form})