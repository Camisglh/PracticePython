from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', blank=True)
    active = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)