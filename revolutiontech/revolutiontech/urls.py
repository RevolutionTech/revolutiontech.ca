"""
:Created: 13 July 2015
:Author: Lucas Connors

"""

from django.conf.urls import include, url
from django.contrib import admin

from basecategory.views import HomeView
from games.views import GamesListView
from productions.views import ProductionsListView
from software.views import SoftwareListView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^games/?$', GamesListView.as_view(), name='games'),
    url(r'^productions/?$', ProductionsListView.as_view(), name='productions'),
    url(r'^software/?$', SoftwareListView.as_view(), name='software'),
    url(r'^/?$', HomeView.as_view(), name='home'),
]
