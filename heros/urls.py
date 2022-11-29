from django.urls import path
from .views import AddHeroView, ListHerosView

urlpatterns = [
    path('add/<str:token>/', AddHeroView.as_view()),
    path('list/<str:token>/', ListHerosView.as_view()),
]