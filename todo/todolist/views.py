from django.shortcuts import render
from django.http import JsonResponse
from .serializers import TodoSerializers, CategorySerializers
from .models import Todo, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST', 'PUT'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializers = CategorySerializers(categories, many=True)
        return JsonResponse({'categories': serializers.data})
    
    elif request.method == 'POST':
        serializers = CategorySerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CategorySerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializers = TodoSerializers(todos, many=True)
        return JsonResponse({'todos': serializers.data})
    
    elif request.method == 'POST':
        serializers = TodoSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializers(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
