from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from conflict.models import Organisation, Article, Conflict

def home(request):
    return render(request, "conflict/home.html")

class OrganisationListView(ListView):
    paginate_by = 10

    def get_queryset(self):
        return Organisation.objects.annotate(conflict_count=Count('conflict')).order_by('-conflict_count')

class ArticleListView(ListView):
    model = Article
    paginate_by = 10

class ConflictListView(ListView):
    model = Conflict

class OrganisationDetailView(DetailView):
    model = Organisation
