# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from conflict.views import OrganisationListView

urlpatterns = patterns('conflict.views',
    url(r'^$', 'home', name='home'),
    url(r'^organisations/$', OrganisationListView.as_view(), name='organisations'),
)
