from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer
from .permissions import IsAuthorOrAdmin
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from like.serializers import LikedUserSerializer
from rest_framework.response import Response
from comment.serializers import CommentSerializer
from like.models import Favorite
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

    @action(['GET'], detail=True)
    def like(self, request, pk):
        post = self.get_object()
        likes = post.likes.all()
        serializer = LikedUserSerializer(instance=likes, many=True)
        return Response(serializer.data, status=200)

    @action(['GET'], detail=True)
    def comment(self, request, pk):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(instance=comments, many=True)
        return Response(serializer.data, status=200)

    @action(['POST', 'DELETE'], detail=True)
    def favorite(self, request, pk):
        post = self.get_object()
        user = request.user
        if request.method == 'POST':
            if user.favorites.filter(post=post).exists():
                return Response('This post already in favorite', status=400)
            Favorite.objects.create(owner=user, post=post)
            return Response('Added to the favorites', status=201)
        elif request.method == 'DELETE':
            favorite = user.favorites.filter(post=post)
            if favorite.exists():
                favorite.delete()
                return Response('You deleted post is Favorites', status=204)
            return Response('Post is not founded', status=404)






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