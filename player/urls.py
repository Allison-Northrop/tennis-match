from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.player_signin, name='player_signin'),
    # url('', views.social.apps.django_app, name='social')),
    url(r'^player_map/$', views.player_map, name='player_map'),
    url(r'^player_details/(?P<pk>\d+)$', views.player_details, name='player_details'),
    url(r'^player_attributes/new/$', views.player_attributes_new, name='player_attributes_new'),
    #do I put a url for the sign in in here?
]
