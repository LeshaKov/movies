from django.shortcuts import render
from django.views.generic import ListView, DetailView

from movies_app.models import Movie
from django.views.generic.base import View


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(is_published=True)
    template_name = 'movies_app/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    template_name = 'movies_app/movie.html'
