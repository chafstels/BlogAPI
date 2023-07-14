from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer
from .permissions import IsAuthorOrAdmin, IsAuthor
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return PostCreateSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [IsAuthorOrAdmin(), permissions.IsAuthenticated()]
        return [permissions.IsAuthenticatedOrReadOnly(),]









# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     def get_serializer_class(self):
#         if self.request.method == "POST":
#             return PostCreateSerializer
#         return PostListSerializer
#
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     lookup_field = 'id'
#
#     def get_permissions(self):
#         if self.request.method == 'DELETE':
#             return (IsAuthorOrAdmin(),)
#         elif self.request.method in ['PUT', 'PATCH']:
#             return (IsAuthor(),)
#         return (permissions.AllowAny(),)
#
#     def get_serializer_class(self):
#         if self.request.method in ['PUT', 'PATCH']:
#             return PostCreateSerializer
#         return PostDetailSerializer