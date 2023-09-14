from django.http import HttpResponse
# Create your views here.
from .models import MovieCategory, MovieOutcast, Movie
from .serializers import MovieCategorySerializer, MovieOutcastSerializer, MovieSerializer
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class MovieOutCastViewSet(viewsets.ModelViewSet):
    queryset = MovieOutcast.objects.all()
    serializer_class = MovieOutcastSerializer

class MovieCategoryViewSet(viewsets.ModelViewSet):
    queryset = MovieCategory.objects.all()
    serializer_class = MovieCategorySerializer    

def Home(request):
    return HttpResponse('Welcome to Hillwood streams')


