from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic.list import ListView
from conflict.models import Organisation, Article

def home(request):
    return HttpResponse("Hi!")

class OrganisationListView(ListView):
    model = Organisation

class ArticleListView(ListView):
    model = Article
