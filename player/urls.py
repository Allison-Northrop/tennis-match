from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.player_signin, name='player_signin'),
]
