from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import PostListCreateView, PostDetailView
from .views import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet)

urlpatterns = [
    # path('', PostListCreateView.as_view()),
    # path('<int:id>/', PostDetailView.as_view()),
    path('', include(router.urls)),
]
