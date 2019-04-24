from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views

app_name = 'movies'

urlpatterns = [
    path('docs/', get_swagger_view(title='movies api docs')),
    path('scores/<int:score_pk>/', views.score_UD),
    path('movies/<int:movie_pk>/scores/', views.score_create),
    path('movies/<int:movie_pk>', views.movie_detail),
    path('movies/', views.movie_list),
    path('genres/<int:genre_pk>', views.genre_detail),
    path('genres/', views.genre_list),
    ]