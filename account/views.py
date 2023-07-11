from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from account.serializers import RegisterSerializer, UserListSerializer, LoginSerializer, UserDetailSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# Create your views here.

class UserRegistration(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Account is created!', status= 200)

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        response_data = {
            'token': token.key,
            'username': user.username,
            'id': user.id,
        }
        return Response(response_data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('you logged out of your account')

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]