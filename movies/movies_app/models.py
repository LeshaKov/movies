from django.db import models
from datetime import date

from django.urls import reverse


class ActorDirector(models.Model):
    """Таблица актеры и режиссеры"""

    name = models.CharField(max_length=150, verbose_name="Полное имя")
    description = models.TextField(verbose_name="Описание")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    image = models.ImageField(upload_to="actors_directors/", verbose_name="Фотография")

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Таблица жанры"""

    name = models.CharField(max_length=100, verbose_name="Жанр")
    description = models.TextField(verbose_name="Описание")
    url = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Category(models.Model):
    """Таблица категории"""

    name = models.CharField(max_length=100, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")
    url = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Таблица фильмы"""

    name = models.CharField(verbose_name="Название", max_length=100)
    tagline = models.CharField(verbose_name="Слоган", max_length=100)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField(verbose_name="Год выхода")
    country = models.CharField(verbose_name="Страна выпуска", max_length=100)
    rating = models.PositiveSmallIntegerField(verbose_name="Рейтинг", default=0)
    world_premiere = models.DateField(default=date.today, verbose_name="Премьера в мире")
    budget = models.DecimalField(verbose_name="Бюджет", help_text="в долларах", max_digits=12,
                                 decimal_places=2, default=0.00)
    fees_usa = models.DecimalField(verbose_name="Сборы с США", help_text="в долларах", max_digits=12,
                                   decimal_places=2, default=0.00)
    fees_world = models.DecimalField(verbose_name="Сборы в мире", help_text="в долларах", max_digits=12,
                                     decimal_places=2, default=0.00)
    url = models.SlugField(unique=True, max_length=100)
    is_published = models.BooleanField(default=False, verbose_name="Публикация")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    actors = models.ManyToManyField(ActorDirector, verbose_name="Актеры", related_name="film_actor")
    directors = models.ManyToManyField(ActorDirector, verbose_name="Режиссеры", related_name="film_director")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.name


class MovieCadres(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=70)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="cadres_movies/")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")

    class Meta:
        verbose_name = "Кадр"
        verbose_name_plural = "Кадры"

    def __str__(self):
        return self.title


class Reviews(models.Model):
    """Таблица отзывов"""

    name = models.CharField(verbose_name="Полное имя", max_length=150)
    email = models.EmailField()
    comment = models.TextField(verbose_name="Отзыв")
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
