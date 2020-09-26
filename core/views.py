
import logging

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from core.forms import MovieForm
from core.models import Movie, AGE_CATEGORIES

logging.basicConfig(
    filename='log.txt',
    filemode='w',
    level=logging.INFO,
)

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Movie
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        return super().form_invalid(form)

class MovieDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser

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


