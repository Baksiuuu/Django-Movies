from django.shortcuts import render
from django.http import HttpResponse
from core.models import Movie

def movies(request):
    return render(
        request,
        template_name = 'movies.html',
        context={'movies': Movie.objects.all()},
    )

