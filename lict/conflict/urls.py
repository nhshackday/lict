# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url, include
from conflict.views import OrganisationListView, ArticleListView, ConflictListView, OrganisationDetailView
from django.http import HttpResponse
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('conflict.views',
    url(r'^robots\.txt', lambda r: HttpResponse('User-agent: *\nDisallow: /', mimetype='text/plain')),
    url(r'^favicon\.ico', lambda r: HttpResponse('', mimetype='image/png')),
    url(r'^$', 'home', name='home'),
    url(r'^organisations/$', OrganisationListView.as_view(), name='organisations'),
    url(r'^organisations/(?P<pk>\d+)/$', OrganisationDetailView.as_view(), name='organisation'),
    url(r'^articles/$', ArticleListView.as_view(), name='articles'),
    url(r'^conflicts/$', ConflictListView.as_view(), name='conflicts'),
    url(r'^stats/$', 'stats', name='stats'),
    url(r'^admin/', include(admin.site.urls)),
)
