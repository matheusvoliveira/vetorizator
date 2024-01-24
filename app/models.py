from django.db import models

class ConvertImage(models.Model):
    originalImage = models.ImageField(upload_to='images/')
    convertedImage = models.FileField(upload_to='converted/')

def get_download_url(self):
    return reverse('download_image', args=[self.id])