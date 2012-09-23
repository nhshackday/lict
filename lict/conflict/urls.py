# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from conflict.views import OrganisationListView, ArticleListView

urlpatterns = patterns('conflict.views',
    url(r'^$', 'home', name='home'),
    url(r'^organisations/$', OrganisationListView.as_view(), name='organisations'),
    url(r'^articles/$', ArticleListView.as_view(), name='articles'),
)
