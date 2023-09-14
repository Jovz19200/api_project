from django.db import models

# Create your models here.
class MovieCategory(models.Model):
    category_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
class Movie(models.Model):
    movie_url = models.URLField()
    trailer_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    category_id = models.ForeignKey(MovieCategory, on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class MovieOutcast(models.Model):
    name = models.CharField(max_length=255)
    avatar_url = models.URLField()
    role = models.CharField(max_length=255)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
