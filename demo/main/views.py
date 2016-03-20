from django.views.generic import DetailView, ListView

from .models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article
