from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.proyectos_list, name='proyectos_list'),
    url(r'^asesor/lista/$', views.asesores_list, name='asesores_list'),
    url(r'^asesor/nuevo/$', views.asesor_nuevo, name='asesor_nuevo'),
    url(r'^proyecto/(?P<pk>[0-9]+)/$', views.proyecto_detail, name='proyecto_detail'),
    #url(r'^asesor/(?P<pk>[0-9]+)/$', views.asesores_detail, name='asesores_detail'),
    path('asesor/<int:pk>/', views.asesores_detail, name='asesores_detail'),
    url(r'^proyecto/nuevo/$', views.proyecto_nuevo, name='proyecto_nuevo'),
    url(r'^proyecto/(?P<pk>[0-9]+)/edit/$', views.proyecto_editar, name='proyecto_editar'),
    url(r'^proyecto/(?P<pk>[0-9]+)/remove/$', views.proyecto_remove, name='proyecto_remove'),
    #url(r'^proyecto/(?P<pk>\d+)/remove/$', views.proyecto_remove, name='proyecto_remove'),
    ]   