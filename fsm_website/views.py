'''This file is used to render the html pages'''
from django.shortcuts import render
from .models import Video


# def index(request):
#     '''This function is used to render the index.html page'''
#     videos = Video.objects.all()
#     return render(request, 'index.html', {'video': videos})

def index(request):
    # Assuming you want to get the latest video, you can use .first()
    video = Video.objects.first()
    return render(request, 'index.html', {'video': video})