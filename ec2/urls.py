from django.conf.urls import url
#from .views import instance,instances,load_balancer,load_balancers
from . import views

urlpatterns = [
    # Examples:
    url(r'^$', views.instance, name='ec2_home'),
    url(r'^instances/$', views.instances),
    url(r'^instances/(?P<instance_id>[-\w]+)$', views.instance),
    url(r'^load-balancers/$', views.load_balancers),
    url(r'^load-balancers/(?P<lb_name>[-\w]+)$', views.load_balancer),
]
