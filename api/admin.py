from django.contrib import admin
from .models import Movie, MovieOutcast, MovieCategory
# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieOutcast)
admin.site.register(MovieCategory)