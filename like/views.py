from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from post.permissions import IsAuthor
# Create your views here.

class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LileDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    lookup_field = 'id'


