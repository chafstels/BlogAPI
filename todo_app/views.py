from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, Todo
from .serializers import CategorySerializer, TodoSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer