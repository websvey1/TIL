from django.shortcuts import render, redirect
from .models import Movie  #?? import models로 해야 하는것 아닌가
# Create your views here.

def index(request):
    movies= Movie.objects.all()
    return render(request, 'movies/index.html', {"movies":movies})

def detail(request, pk):
    movies = Movie.objects.get(pk=pk) 
    return render(request, 'movies/detail.html', {'movies':movies})

def delete(request, pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('/movies/', {'movies':movies})