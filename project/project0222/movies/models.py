from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=15)
    audience = models.IntegerField()
    genre = models.CharField(max_length=10)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    def __str__(self):
        return f'{self.id}: {self.title}'
    