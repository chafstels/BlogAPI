from rest_framework import serializers
from .models import Category, Todo


class CategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Todo
        fields = '__all__'
