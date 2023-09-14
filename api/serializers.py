from rest_framework import serializers
from .models import Movie, MovieOutcast, MovieCategory


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'release_date', 'description', 'category_id', 'movie_url', 'trailer_url', 'created_at')

class MovieOutcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieOutcast
        fields = '__all__'

class MovieCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategory
        fields = '__all__'
