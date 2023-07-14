from django.urls import path
from .views import LikeCreateView, LileDeleteView


urlpatterns = [
    path('', LikeCreateView.as_view()),
    path('<int:id>/', LileDeleteView.as_view()),

]