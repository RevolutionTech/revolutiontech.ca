"""
:Created: 13 July 2015
:Author: Lucas Connors

"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

from basecategory.views import HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^games/', include('games.urls', namespace='games')),
    url(r'^productions/', include('productions.urls', namespace='productions')),
    url(r'^software/', include('software.urls', namespace='software')),
    url(r'^$', HomeView.as_view(), name='home'),
]

# Add media folder to urls when DEBUG = True
if settings.DEBUG:
    urlpatterns.append(
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    )
