from rest_framework import serializers
from . import models


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = (
                    'id',
                    'first_name',
                    'last_name'
                )

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=True, read_only=True)
    date_published = serializers.DateField(input_formats=['%Y-%m-%d'])
    class  Meta:
        model = models.Movie
        fields = (
                    'id',
                    'movie_name',
                    'review',
                    'description',
                    'date_published',
                    'director'
                )
        