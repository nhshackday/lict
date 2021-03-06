from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from conflict.models import Organisation, Article, Conflict

def home(request):
    return render(request, "conflict/home.html")

def stats(request):
    context = {}
    context['organisation_count'] = Organisation.objects.count()
    context['real_organisation_count'] = Organisation.real_organisations.count()
    context['article_count'] = Article.objects.count()
    return render(request, 'conflict/stats.html', context)


class OrganisationListView(ListView):
    paginate_by = 10

    def get_queryset(self):
        return Organisation.real_organisations.annotate(conflict_count=Count('conflict')).order_by('-conflict_count')

class ArticleListView(ListView):
    model = Article
    paginate_by = 10

class ConflictListView(ListView):
    model = Conflict

class OrganisationDetailView(DetailView):
    model = Organisation
