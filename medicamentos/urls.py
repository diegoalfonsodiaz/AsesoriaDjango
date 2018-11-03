from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.proyectos_list, name='proyectos_list'),
    url(r'^asesor/lista/$', views.asesores_list, name='asesores_list'),
    url(r'^asesor/nuevo/$', views.asesor_nuevo, name='asesor_nuevo'),
    ]   