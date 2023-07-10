from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=8, write_only=True)
    password_confirmation = serializers.CharField(required=True, min_length=8, write_only=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password_confirmation')

    def validate(self, attrs):
        password_confirmation = attrs.pop('password_confirmation')
        if password_confirmation != attrs['password']:
            raise serializers.ValidationError(
                'Passwords do not match'
            )
        if not attrs['first_name'].istitle():
            raise serializers.ValidationError(
                'The name must begin with a capital letter'
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'