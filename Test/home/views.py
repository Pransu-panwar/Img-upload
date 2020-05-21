from django.shortcuts import render
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def uploadImage(request):
    print('Request Handling...........')
    if request.method == 'POST':
        p = request.FILES['image']

        user = User(pic =p)
        user.save()
        messages.success(request, 'File uploaded successfully')
    else:
        messages.success(request, 'No upload')
    return render(request,'upload.html')