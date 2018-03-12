from django.conf.urls import url,include
from .views import home, register, dash, userdash, auth_dash,mys3

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
    url(r'^authdash/', auth_dash),
    url(r'^dash/', dash, name='dash'),
    url(r'^userdash/', userdash, name='userdash'),
    url(r'^mys3/', mys3),
]
