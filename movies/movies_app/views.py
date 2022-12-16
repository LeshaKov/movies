from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from movies_app.models import Movie
from .forms import ReviewForm


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(is_published=True)
    template_name = 'movies_app/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    template_name = 'movies_app/movie.html'


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
