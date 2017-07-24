from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.player_signin, name='player_signin'),
    url(r'^player_map/$', views.player_map, name='player_map'),
    url(r'^player_details/(?P<pk>\d+)$', views.player_details, name='player_details'),
    url(r'^player_attributes/new/$', views.player_attributes_new, name='player_attributes_new'),
    #do I put a url for the sign in in here?
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^player_attributes_edit/(?P<pk>\d+)/edit/$', views.player_attributes_edit, name='player_attributes_edit'),
]
