# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from conflict.views import OrganisationListView, ArticleListView, ConflictListView, OrganisationDetailView

urlpatterns = patterns('conflict.views',
    url(r'^$', 'home', name='home'),
    url(r'^organisations/$', OrganisationListView.as_view(), name='organisations'),
    url(r'^organisations/(?P<pk>\d+)/$', OrganisationDetailView.as_view(), name='organisation'),
    url(r'^articles/$', ArticleListView.as_view(), name='articles'),
    url(r'^conflicts/$', ConflictListView.as_view(), name='conflicts'),
)
