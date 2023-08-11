from django.contrib import admin
from .models import Anime, Genre, AnimeName

class AnimeAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres',) # добавляем возможность выбора нескольких жанров

admin.site.register(Genre)
admin.site.register(Anime, AnimeAdmin)
admin.site.register(AnimeName)