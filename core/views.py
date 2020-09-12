from concurrent.futures._base import LOGGER

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView

from core.forms import MovieForm
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

class MovieCreateView(FormView):
    title = 'Add Movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.object.create(
            title = cleaned_data['title'],
            genre = cleaned_data['genre'],
            rating = cleaned_data['rating'],
            released = cleaned_data['released'],
            description = cleaned_data['description'],
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['limits'] = AGE_CATEGORIES
        return context


















