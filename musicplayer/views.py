from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

# Create your views here.
def index(request):
    return HttpResponse("Hello, you're at the musicplayer index")