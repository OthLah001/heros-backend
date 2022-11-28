from django.urls import path
from .views import LoginView, InitView, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('check_token/<str:token>/', LoginView.as_view()),
    path('init/<str:token>/', InitView.as_view()),
    path('signup/', SignUpView.as_view())
]