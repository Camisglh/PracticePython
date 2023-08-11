from django.shortcuts import render, redirect
from .models import Anime
from django.db.models import Q
from .forms import Animecreate
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

def index(request):
    anime = Anime.objects.all()
    context = {'anime': anime}
    return render(request, 'anime/bases/home.html', context)

def search(request):
    query = request.GET.get('q')
    animes = Anime.objects.filter(Q(author__username__icontains=query))
    return render(request, 'anime/bases/searchresult.html', {'animes': animes})

def animcreate(request):
    if request.method == 'POST':
        form = Animecreate(request.POST, request.FILES)
        if form.is_valid():
            anime = form.save(commit=False)
            anime.author = request.user
            anime.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = Animecreate()
    return render(request, 'anime/bases/animcreate.html', {'form': form})


class AnimeUpdateView(UpdateView):
    model = Anime
    fields = ['name', 'status', 'description', 'genres', 'rating', 'studios', 'dubbing']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')