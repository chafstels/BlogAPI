from django.urls import path
from .views import UserRegistration, UserListAPIView, LoginView, LogoutView, UserDetailView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', UserRegistration.as_view()),
    path('list_users/', UserListAPIView.as_view()),
    # path('login/', ObtainAuthToken.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('<int:id>/', UserDetailView.as_view()),
]