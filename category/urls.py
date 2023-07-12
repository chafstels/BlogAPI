from django.urls import path, include
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .views import CategoryCreateListView, CategoryDetailView



urlpatterns = [
    path('', CategoryCreateListView.as_view()),
    path('<int:id>/', CategoryDetailView.as_view()),
]