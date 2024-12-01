from django.shortcuts import render, redirect
from .models import Multimedia
from .forms import MultimediaForm

def home(request):
    multimedia = Multimedia.objects.all()
    return render(request, 'media_app/home.html', {'multimedia': multimedia})

def upload_media(request):
    if request.method == 'POST':
        form = MultimediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MultimediaForm()
    return render(request, 'media_app/upload.html', {'form': form})
