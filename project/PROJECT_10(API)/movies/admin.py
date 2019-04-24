from django.contrib import admin
from .models import Movie, Genre, Score
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'audience', 'poster_url', 'description']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['content', 'score']

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Score, ScoreAdmin)