from django.shortcuts import render
from .models import Comment
from rest_framework import generics, permissions
from .serializers import CommentSerializer
from post.permissions import IsAuthor, IsAuthorOrAdminPostOwner


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthorOrAdminPostOwner(),)
        return (permissions.AllowAny(),)
