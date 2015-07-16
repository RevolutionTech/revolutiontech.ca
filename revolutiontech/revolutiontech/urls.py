"""
:Created: 13 July 2015
:Author: Lucas Connors

"""

from django.conf.urls import include, url
from django.contrib import admin

from basecategory.views import HomeView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?', HomeView.as_view()),
]
