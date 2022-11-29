from django.urls import path
from .views import AddHeroView, ListHerosView, HeroView, HeroRatingView

urlpatterns = [
    path('add/<str:token>/', AddHeroView.as_view()),
    path('list/<str:token>/', ListHerosView.as_view()),
    path('get/<int:id>/<str:token>/', HeroView.as_view()),
    path('rate/<str:token>/', HeroRatingView.as_view()),
]