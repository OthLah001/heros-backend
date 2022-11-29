from django.urls import path
from .views import AddHeroView, ListHerosView, HeroView

urlpatterns = [
    path('add/<str:token>/', AddHeroView.as_view()),
    path('list/<str:token>/', ListHerosView.as_view()),
    path('get/<int:id>/<str:token>/', HeroView.as_view()),
]