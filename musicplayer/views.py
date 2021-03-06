from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Song

# Create your views here.
def index(request):
    song_list = Song.objects.all()
    paginator = Paginator(song_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)