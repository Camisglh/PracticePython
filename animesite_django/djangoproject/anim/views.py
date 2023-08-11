from django.shortcuts import render
from .models import Anime
# Create your views here.
def index(request):
    anime = Anime.objects.all()
    context = {'anime': anime}
    return render(request, 'anime/base/bases.html', context)