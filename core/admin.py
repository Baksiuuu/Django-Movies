from django.contrib import admin
from django.urls import path
from core.models import Movie, Genre
from core.views import hello

admin.site.register(Movie)
admin.site.register(Genre)