from concurrent.futures._base import LOGGER
import logging

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

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

# class MovieCreateView(FormView):
#     title = 'Add Movie'
#     template_name = 'form.html'
#     form_class = MovieForm
#     success_url = reverse_lazy('movie_create')
#
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cleaned_data = form.cleaned_data
#         Movie.objects.create(
#             title = cleaned_data['title'],
#             genre = cleaned_data['genre'],
#             rating = cleaned_data['rating'],
#             released = cleaned_data['released'],
#             description = cleaned_data['description'],
#         )
#         return result
#
#     def form_invalid(self, form):
#         LOGGER.warning('Invalid data provided.')
#         return super().form_invalid(form)

logging.basicConfig(
    filename='log.txt',
    filemode='w',
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)


class MovieCreateView(CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['limits'] = AGE_CATEGORIES
        return context

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie


