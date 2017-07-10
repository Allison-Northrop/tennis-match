from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.player_signin, name='player_signin'),
    url(r'^player_attributes/new$', views.player_attributes_new, name='player_attributes_new'),
]
