from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models

# Create your views here.

class MovieView(generics.CreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
