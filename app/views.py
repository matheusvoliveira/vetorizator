from django.shortcuts import render
from django.http import HttpResponse
from wand.image import Image
import tempfile
import os
from .models import ConvertImage
from django import forms 
from django.shortcuts import render, redirect
from .forms import ImageForm
import convertapi
from django.http import HttpResponse
from io import BytesIO
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import ConvertImage
import os 
import glob
import mimetypes
from django.http import FileResponse
# from django.core.servers.basehttp import FileWrapper
import mimetypes
import os
from django.core.files.storage import default_storage

def index(request):
    return render(request, 'index.html')

def download_image(request):
    return render(request, 'download_image.html')

def upload_button(request):
    return render(request, 'upload-button.html')

class ConvertImageForm(forms.ModelForm):
    class Meta:
        model = ConvertImage
        fields = ['originalImage', 'convertedImage']

def upload_image(request):
    directory_path = 'cache_imgs'
    files = glob.glob(os.path.join(directory_path, '*'))
    for file in files:
        if os.path.isfile(file):
            os.remove(file)
    ConvertImage.objects.all().delete()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form_submitted = True
            form.save()
            convert(request)
            return render(request, "download_image.html")
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def convert(request):
    # Assuming ConvertImage has a OneToOneField with User model
    image_original = ConvertImage.objects.latest('originalImage')
    image_converted = ConvertImage.objects.latest('convertedImage')
    # Get the file path of the originalImage
    file_path_original = image_original.originalImage.path
    # file_path_converted = image_converted.convertedImage.path
    # Convert the image to SVG using convertapi
    convertapi.api_secret = 'dqgG1I15SKCjpaPH'
    convertapi.convert('svg', {'File': file_path_original}, from_format='png').save_files('cache_imgs')
    #     print(f"An error occurred: {e}"
    # # Prepare the response
    # if result['Files']:
    #     svg_content = result['Files'][0]['FileContent']

    #     # Prepare the response
    #     response = HttpResponse(content_type='image/svg+xml')
    #     response['Content-Disposition'] = 'attachment; filename="converted_image.svg"'

    #     # Write the SVG content to the response
    #     response.write(svg_content)

    #     return response
    # else:
    #     # Handle the case where conversion failed
    #     return HttpResponse("Conversion failed")
    # # Delete all ConvertImage objects

# your_app/views.py
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from .models import ConvertImage

# def download_last_image(request):
#     # Get the last image from the database
#     last_image = ConvertImage.objects.order_by('-originalImage').first()

#     if last_image:
#         # Prepare the response for the image file
#         response = HttpResponse(content_type='application/octet-stream')
#         response['Content-Disposition'] = f'attachment; filename="{last_image.originalImage.name}"'
        
#         # Write the image file content to the response
#         with open(last_image.originalImage.path, 'rb') as file:
#             response.write(file.read())

#         return response
#     else:
#         # Handle the case where no image is found
#         return HttpResponse("No image available for download")


def download_last_image(request):
    directory_path = 'C:/Users/Matheus/Documents/vetorizator/cache_imgs'
    files = glob.glob(os.path.join(directory_path, '*'))
    files.sort()
    if files:
        file_path = files[0]
        filename = os.path.basename(file_path)
        response = FileResponse(open(file_path, 'rb'), content_type='image/svg+xml')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
    else:
        return HttpResponse('No file in this repository')