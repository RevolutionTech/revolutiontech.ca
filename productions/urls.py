"""
:Created: 26 July 2015
:Author: Lucas Connors

"""

from django.urls import path

from basecategory.views import ItemPageView
from productions.models import Production
from productions.views import ProductionsListView

app_name = "productions"
urlpatterns = [
    path(
        "<slug:slug>/",
        ItemPageView.as_view(),
        {"items": Production},
        name="item_details",
    ),
    path(
        "",
        ProductionsListView.as_view(),
        {"items": Production},
        name="productions_list",
    ),
]
