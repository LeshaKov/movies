from django.contrib import admin
from .models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("id", "name", "year", "country", "rating", "url", "is_published", "category")
    search_fields = ("name", "category__name")
    list_editable = ("is_published",)
    list_filter = ("category", "year", "rating", "genres")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("id", "name", "url")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(MovieCadres)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("id", "title", "movie", "image")


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("id", "name", "email", "parent", "movie")
    readonly_fields = ("name", "email")


@admin.register(ActorDirector)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ("id", "name", "age", "image")
