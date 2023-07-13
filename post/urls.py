from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<int:id>/', PostDetailView.as_view()),
]
