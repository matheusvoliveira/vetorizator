from django.db import models 

class ConvertImage(models.Model):
    originalImage = models.ImageField(upload_to='images/')
    convertedImage = models.ImageField(upload_to='images/')

