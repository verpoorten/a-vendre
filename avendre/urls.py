"""
avendre URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from livres.views import LivresList
from django.conf import settings
from django.conf.urls.static import static
from livres.views import home
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'livres/', include('livres.urls')),
    url(r'admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
