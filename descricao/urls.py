from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^home$', views.index, name = 'home'),
    url(r'^adicionar$', views.adicionar, name='adicionar'),
    url(r'^mossad$', views.mossad, name='mossad'),
    url(r'^adicionar_mossad$', views.adicionar_mossad, name='adicionar_mossad'),
    url(r'^mi5$', views.mi5, name='mi5'),
    url(r'^adicionar_mi5$', views.adicionar_mi5, name='adicionar_mi5'),
    url(r'^search_mossad', views.search_mossad, name='search_mossad'),
    url(r'^search_mi5', views.search_mi5, name='search_mi5'),
]