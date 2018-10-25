from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'livres/', views.LivresList.as_view(), name='livres'),
    url(r'auteurs/', views.AuteursList.as_view(), name='auteurs'),
    url(r'^livre/(?P<pk>\d+)/detail/$', views.LivreDetail.as_view(),
        name='livre_detail'),
    url(r'^livre/(?P<pk>\d+)/edit/$', views.EditLivre.as_view(),
        name='edit_livre'),
    url(r'^livre_search/$', views.livre_search, name='livre_search'),
    url(r'^favoris/$', views.favoris, name='favoris'),

]
