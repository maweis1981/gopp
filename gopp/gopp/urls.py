from django.conf.urls import patterns, include, url
from django.contrib import admin

import phonegame
from phonegame import urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gopp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^phonegame/', include(phonegame.urls)),
)
