from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^example/(?P<id>\d+)', 'angular.views.example'),
    url(r'^$', 'angular.views.home'),
)