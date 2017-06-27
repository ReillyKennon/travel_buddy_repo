from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^home$', views.home, name='home'),
    url(r'^add$', views.add, name='add'),
    url(r'^destination$', views.destination, name='destination'),
    url(r'^addplan$', views.addplan, name='addplan'),
]
