from django.conf.urls import patterns, url

from phonegame import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<poll_id>\d+)/$',views.detail,name='detail'),
)