from django.contrib import admin
from .models import Anime, AnimeName, Studio, Genre
from .forms import AnimeForm

class AnimeAdmin(admin.ModelAdmin):
    form = AnimeForm

admin.site.register(Anime, AnimeAdmin)
admin.site.register(AnimeName)
admin.site.register(Studio)
admin.site.register(Genre)