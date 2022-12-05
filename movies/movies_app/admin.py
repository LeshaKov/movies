from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(ActorDirector)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieCadres)
admin.site.register(Reviews)

