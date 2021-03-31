from django.shortcuts import render

from .models import Song

# Create your views here.
def index(request):
    context = {
        'song_list': Song
    }
    return render(request, 'index.html', context)