from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic.list import ListView
from conflict.models import Organisation

def home(request):
    return HttpResponse("Hi!")

class OrganisationListView(ListView):
    model = Organisation
