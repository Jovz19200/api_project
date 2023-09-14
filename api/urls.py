from django.urls import path

from .views import  MovieViewSet, MovieOutCastViewSet, MovieCategoryViewSet, Home

urlpatterns = [
    path('', Home),
    path('api/movies', MovieViewSet.as_view({'get': 'list',
        'post':'create',
        'put': 'update',
        'delete': 'destroy',})),
         #use '/api/movies' to view movies in movies api
    path('api/movies/category', MovieCategoryViewSet.as_view({
        'get': 'list',
        'post':'create',
        'put': 'update',
        'delete': 'destroy',
        })),

        #use '/api/movies/category' to view info category api
    path('api/movies/cast', MovieOutCastViewSet.as_view({
        'get': 'list',
        'post':'create',
        'put': 'update',
        'delete': 'destroy',}))
         #use '/api/movies/cast' to view info about cast in cast api
]