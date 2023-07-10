from django.urls import include, path
from rest_framework import routers
from todo_app.views import CategoryViewSet, TodoViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'todos', TodoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]