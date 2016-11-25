from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^updateDB/$', views.updateDB, name='updateDB'),
    # url(r'^fit/$', views.fit, name='fit'),
    url(r'^filtro/$', views.filtro, name='filtro'),
    url(r'^(?P<nomeDoenca>[A-Z][a-z]+)/$', views.medicamentos, name='medicamentos'),
]