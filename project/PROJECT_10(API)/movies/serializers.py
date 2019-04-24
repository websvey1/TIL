from rest_framework import serializers
from .models import Movie, Genre, Score

class Genreserializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']
    
class Movieserializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','audience','poster_url','genre','description']

class GenreDetailserializers(serializers.ModelSerializer):
    movie_set = Movieserializers(many=True)
    class Meta:
        model = Genre
        fields = ['id' ,'movie_set']

# class MovieDetailserializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = Movie
#         fields = ['id','title','']

class Scoreserializers(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id','content', 'score']