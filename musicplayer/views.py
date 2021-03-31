from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Song

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'song_list': Song
    }
    return HttpResponse(template.render(context, request))