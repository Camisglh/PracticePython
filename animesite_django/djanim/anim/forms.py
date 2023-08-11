from django import forms
from django.contrib.auth.models import User
from .models import Anime

class Animecreate(forms.ModelForm):
    class Meta:
     model = Anime
     fields = ('name', 'status', 'rating', 'image', 'genres', 'dubbing', 'studios', 'description')