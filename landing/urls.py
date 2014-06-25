#-*- coding: cp1251-*-
from django.conf.urls import patterns, include, url
from landing.views import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'landing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', view, {'city':None}),
    url(r'^(?P<city>\w+)/$', view),
    url(r'^admin/', include(admin.site.urls)),
)
