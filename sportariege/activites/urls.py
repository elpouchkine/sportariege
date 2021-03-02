from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.activites, name='activites'),
    url(r'^(?P<Activite>\w+)/$', views.activite, name='activite')
]