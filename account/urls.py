from django.urls import path, include
from .views import UserRegistration, UserListAPIView, UserDetailView, UserViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UserViewSet)


urlpatterns = [
    path('register/', UserRegistration.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    # path('list_users/', UserListAPIView.as_view()),
    # path('login/', ObtainAuthToken.as_view()),
    # path('login/', LoginView.as_view()),
    # path('logout/', LogoutView.as_view()),
    # path('<int:id>/', UserDetailView.as_view()),
    path('', include(router.urls)),
]