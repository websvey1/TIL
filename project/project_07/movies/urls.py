from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/comments/<int:score_pk>/delete', views.comments_delete, name='comments_delete'),
    path('<int:movie_pk>/comments/', views.comments_create, name='comments_create'),    
    path('<int:movie_pk>/delete', views.delete, name='delete'),             #4 detail은 주소 뒤에 바로 /숫자/가 붙는제 delete는 숫자뒤에 delete가 붙게끔 설정
                                                                            #4 #### views.py로 이동
    path('<int:movie_pk>/', views.detail, name='detail'),                #2 인덱스에서 제목을 클릭하면 링크의 url을 요청하고, <int:movie_pk>에서 movie_pk는 views로 넘어가는 단순히 변수명이다. 
    path('', views.index, name="index"),                                 #2 urls.py에서 정의된 형식에 따라 views.py로 넘어간다.
                                                                         ###### views.py로 이동 #####
]