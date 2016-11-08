from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^updateDB/$', views.updateDB, name='updateDB'),
    url(r'^fit/$', views.fit, name='fit'),
]