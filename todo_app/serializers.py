from rest_framework import serializers
from .models import Category, Todo
class CategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class TodoSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Todo
        fields = '__all__'