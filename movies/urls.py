from django.urls import path
from . import views


urlpatterns = [
    path("movies/", views.MovieView.as_view()),
    path("movies/<int:movie_id>/", views.MovieParamView.as_view()),
    path("movies/<int:movie_id>/orders/", views.MovieOrderParamView.as_view()),
]
