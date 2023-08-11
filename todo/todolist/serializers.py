from rest_framework import serializers
from .models import Todo, Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'description', 'image', 'active', 'category', 'data', 'data_update']