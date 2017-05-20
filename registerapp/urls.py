from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^getclients/', views.get_clients , name = 'getclients'),
    url(r'^modelform/' , views.model_form , name = ' modelform'),
    url(r'^login/', views.login, name='login'),
]