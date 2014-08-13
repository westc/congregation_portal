from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from congregation_portal import views
from congregation_portal import settings


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^auth/$', views.auth_and_login),
    url(r'^$', views.index),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()