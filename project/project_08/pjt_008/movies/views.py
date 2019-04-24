from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Genre, Movie, Score
from django.db.models import Avg
from .forms import MovieForm, ScoreForm
# Create your views here.
def index(request):
    movies =get_list_or_404(Movie.objects.annotate(score_avg=Avg('score__score')))
    context = {
        'movies':movies
        }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {'form':form}
    return render(request, 'movies/form.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie.objects.annotate(score_avg=Avg('score__score')), pk=movie_pk)
    form = ScoreForm()
    scores = movie.score_set.all()
    context = {'movie':movie, 'form':form, 'scores':scores}
    
    return render(request, 'movies/detail.html', context)
    
    
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)
        
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {'form':form, 'movie':movie}
    return render(request, 'movies/form.html', context)

def comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        score = Score(movie=movie)
        form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            score = form.save()
            return redirect('movies:detail', movie.pk)
    return redirect('movies:detail', movie.pk)

def comments_delete(request, movie_pk, score_pk):
    comment = Score.objects.get(pk=score_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('movies:detail', movie_pk)
    else:
        return redirect('movies:detail', movie_pk)