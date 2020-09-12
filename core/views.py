from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Movie, AGE_CATEGORIES


# class MovieView(views.View):
#     def get(self, request):
#         return render(
#             request,
#             template_name = 'movies.html',
#             context={'movies': Movie.objects.all(), 'limits': AGE_CATEGORIES},
#     )
# )

class MovieView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all(), 'limits': AGE_CATEGORIES}

