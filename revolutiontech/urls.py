"""
:Created: 13 July 2015
:Author: Lucas Connors

"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from basecategory.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("games/", include("games.urls", namespace="games")),
    path("productions/", include("productions.urls", namespace="productions")),
    path("software/", include("software.urls", namespace="software")),
    path("", HomeView.as_view(), name="home"),
]

# Add media folder to urls when DEBUG = True
if settings.DEBUG:
    urlpatterns.append(
        re_path("^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})
    )
