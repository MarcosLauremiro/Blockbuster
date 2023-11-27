from django.urls import path
from rest_framework_simplejwt import views

from .views import MovieDetailViel, MovieView


urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailViel.as_view()),
]





