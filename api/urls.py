from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.MovieView.as_view(), name='movieView')
]

