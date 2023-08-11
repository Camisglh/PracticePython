from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

class Status(models.TextChoices):
    VIEWED = 'Смотрю', 'Смотрю'
    UNVIEWED = 'Просмотрено', 'Просмотрено'
    DISLIKE = 'Бросил', 'Бросил'

class Rating(models.IntegerChoices):
    ONE = 1, '1'
    TWO = 2, '2'
    THREE = 3, '3'
    FOUR = 4, '4'
    FIVE = 5, '5'

class AnimeName(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Anime(models.Model):
    name = models.ForeignKey(AnimeName, on_delete=models.CASCADE)
    status = models.CharField(max_length=250, choices=Status.choices, default=Status.UNVIEWED)
    rating = models.IntegerField(choices=Rating.choices, default=Rating.FIVE)
    genres = models.ManyToManyField(Genre)
    studios = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя: {self.name} Автор: {self.author}'

class AnimeForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Anime
        fields = '__all__'