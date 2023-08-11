from django import forms
from django.forms import CheckboxSelectMultiple
from .models import Anime, Genre

class AnimeForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Anime
        fields = '__all__'