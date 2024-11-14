from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedFile
from .forms import FileUploadForm

def home(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    files = UploadedFile.objects.all()
    return render(request, 'fileupload/home.html', {'form': form, 'files': files})
