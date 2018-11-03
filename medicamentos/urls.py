from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^asesor/nuevo/$', views.asesor_nuevo, name='asesor_nuevo'),
    ]   