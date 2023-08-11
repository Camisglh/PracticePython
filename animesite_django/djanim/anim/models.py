from django import forms
from django.db import models
from django.contrib.auth.models import User

class Status(models.TextChoices):
    VIEWED = 'Смотрю', 'Смотрю'
    UNVIEWED = 'Просмотрено', 'Просмотрено'
    DISLIKE = 'Бросил', 'Бросил'

class Rating(models.IntegerChoices):
    ONE = 1, '1'
    TWO = 2, '2'
    THREE = 3, '3'
    FOUR = 4, '4'
    FIVE = 5

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Dubbing(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AnimeName(models.Model):
    name = models.CharField(max_length=250)

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
    genres = models.ManyToManyField(Genre, related_name='animes')
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    dubbing = models.ManyToManyField(Dubbing, related_name='animes')
    studios = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя: {self.name} Автор: {self.author}'


class AnimeForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    dubbing = forms.ModelMultipleChoiceField(
        queryset=Dubbing.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Anime
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        anime_name = self.cleaned_data['name']
        genres = self.cleaned_data['genres']
        dubbing = self.cleaned_data['dubbing']
        anime_name = AnimeName.objects.create(name=anime_name)
        anime_name.genres.set(genres)
        instance.name = anime_name
        instance.dubbing.set(dubbing)
        if commit:
            instance.save()
        return instance