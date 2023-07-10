from django.urls import path
from .views import UserRegistration, UserListAPIView


urlpatterns = [
    path('register/', UserRegistration.as_view()),
    path('list_users/', UserListAPIView.as_view())

]