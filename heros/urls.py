from django.urls import path
from .views import AddHeroView

urlpatterns = [
    path('add/<str:token>/', AddHeroView.as_view()),
]