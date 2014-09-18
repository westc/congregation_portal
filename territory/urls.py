from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

from territory import views

urlpatterns = patterns(
    '',
    url(r'^$', views.territory_reports),
    url(r'reports/$', views.territory_reports),
)
