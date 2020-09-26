from core.models import Movie
from core.views import MovieListView


class IndexView(MovieListView):
    template_name = 'index.html'
    model = Movie