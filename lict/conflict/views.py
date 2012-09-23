from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from conflict.models import Organisation, Article, Conflict

def home(request):
    return HttpResponse("Hi!")

class OrganisationListView(ListView):
    model = Organisation
    paginate_by = 10

class ArticleListView(ListView):
    model = Article
    paginate_by = 10

class ConflictListView(ListView):
    model = Conflict

class OrganisationDetailView(DetailView):
    model = Organisation
