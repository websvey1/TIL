from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Score
from .serializers import Genreserializers, Movieserializers, GenreDetailserializers, Scoreserializers
# Create your views here.
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.order_by('pk')
    serializer = Genreserializers(genres, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genre_detail(request, genre_pk):
    genres = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailserializers(genres)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.order_by('pk')
    serializer = Movieserializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    serializer = Movieserializers(movies)
    return Response(serializer.data)

@api_view(['POST'])
def score_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = Scoreserializers(data=request.data) # data 앞에 왜 movie를 넣는다고 생각했지??
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk)   # 이부분 이해가 안됀디....
        return Response({'message':'댓글이 작성되었습니다'}) # 괄호안에는 단순히 결과값출력창

@api_view(['PUT','DELETE'])
def score_UD(request, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    if request.method =='PUT':
        serializer = Scoreserializers(data=request.data, instance=score)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'수정되었습니다.'})
    else:
        score.delete()
        return Response({'message':'삭제되었습니다.'})
