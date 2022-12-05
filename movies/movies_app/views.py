from django.shortcuts import render
from movies_app.models import Movie
from django.views.generic.base import View


class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        print(movies)
        return render(request, 'movies_app/movie_list.html', context={"movie_list": movies})

