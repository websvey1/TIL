from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Score, Genre, Movie
# Create your views here.
def index(request):                                     #1 인덱스 정의 / 요청을 받으면
    # movies = Movie.objects.order_by('-pk')              #1 movies라는 변수에 models의 Movie  클래스 오브젝트를 pk(기본키)의 내림차순으로 정렬.
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    # score테이블의 score컬럼(score__score)의 평균을 score__avg라는 새로운 컬럼으로 추가적을 붙여서 (annotate) , 모든 데이터의 결과를 받아보겟다 라는 뜻
                                                        #1 즉 movies는 모델의 Movie클래스의 기본키(pk)이다.
    context = {                                         #1 context라는 dict에 movies 변수를 'movies'라는 키값에 담아서
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context) #1 movies(templates안에있는)/index.html로 보낸다 
                                                         ###  index.html로 이동 ####

def detail(request, movie_pk):                              #3 url로 detail을 요청받으면 return할 결과를 정의, movie_pk는 url에서 정의한 변수 !.
    # movie = Movie.objects.get(pk=movie_pk)                #3 index.html에서 영화제목을 클릭하면서 입력된 영화기본키에 있는 모든 데이터를 movie변수로 저장
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)
    genre = Genre.objects.get(pk=movie.genre_id)            #3 ??
    scores = movie.score_set.all()                          #3 ??
    context ={                                              #3 context dict에 변수명의 키로 넣는다
        'movie': movie,
        'scores':scores,
        'genre':genre
    }
    return render(request, 'movies/detail.html', context)   #3 이 데이터를 detail.html로 보낸다
                                                            ######3 detail.html로 이동 ###########
def delete(request, movie_pk):                               
    movie = Movie.objects.get(pk=movie_pk)                  #4 movie변수에 기본키를 포함한 모든 데이터 저장
    if request.method == 'POST':                            #4 POST방식이면 지우고 인덱스 화면을 띄우고
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)          #4 GET방식이면 =(detail.html에 삭제확인 버튼이 POST방식이라고 되있으므로) 디테일 화면을 띄움
                                                            ##### detail.html로 이동 #####
def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    content = request.POST.get('content')
    score = request.POST.get('score')
    scores = Score(movie=movie, content=content, score=score)
    scores.save()
    return redirect('movies:detail', movie.pk)

def comments_delete(request, movie_pk, score_pk):
    comment = Score.objects.get(pk=score_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('movies:detail', movie_pk)
    else:
        return redirect('movies:detail', movie_pk)
        
    
    