from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/comments_delete/<int:score_pk>', views.comments_delete, name='comments_delete'),
    path('<int:movie_pk>/comments', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/edit/', views.update, name='update'),
    path('<int:movie_pk>/delete', views.delete, name='delete'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('', views.index, name='index'),
]