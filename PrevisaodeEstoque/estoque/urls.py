from django.conf.urls import url

from . import views

app_name='estoque'
urlpatterns = [
    # url(r'^updateDB/$', views.updateDB, name='updateDB'),
    # url(r'^fit/$', views.fit, name='fit'),
    url(r'^filtro/$', views.filtro, name='filtro'),
    url(r'^equipe/$', views.equipe, name='equipe'),
    url(r'^help/$', views.help, name='help'),
    url(r'^mapa/$', views.mapa, name='mapa'),
    url(r'^medicamentos/(?P<nomeDoenca>([A-Z])\w*)/$', views.medicamentos, name='medicamentos'),
    url(r'^previsao/(?P<registro>[0-9]+)/$', views.previsao, name='previsao'),
]