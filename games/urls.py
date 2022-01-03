"""
:Created: 26 July 2015
:Author: Lucas Connors

"""

from django.urls import path

from basecategory.views import ItemPageView
from games.models import Game
from games.views import GamesListView

app_name = "games"
urlpatterns = [
    path("<slug:slug>/", ItemPageView.as_view(), {"items": Game}, name="item_details"),
    path("", GamesListView.as_view(), {"items": Game}, name="games_list"),
]
