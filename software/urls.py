"""
:Created: 26 July 2015
:Author: Lucas Connors

"""

from django.urls import path

from basecategory.views import ItemPageView
from software.models import Software
from software.views import SoftwareListView

app_name = "software"
urlpatterns = [
    path(
        "<slug:slug>/",
        ItemPageView.as_view(),
        {"items": Software},
        name="item_details",
    ),
    path("", SoftwareListView.as_view(), {"items": Software}, name="software_list"),
]
