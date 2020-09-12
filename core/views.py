from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from core.models import Movie, AGE_CATEGORIES


# class MovieView(views.View):
#     def get(self, request):
#         return render(
#             request,
#             template_name = 'movies.html',
#             context={'movies': Movie.objects.all(), 'limits': AGE_CATEGORIES},
#     )
# )

# class MovieView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all(), 'limits': AGE_CATEGORIES}

class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['limits'] = AGE_CATEGORIES
        return context



















