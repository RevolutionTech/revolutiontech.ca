"""
:Created: 26 July 2015
:Author: Lucas Connors

"""

from django.conf.urls import url

from basecategory.views import ItemPageView
from games.models import Game
from games.views import GamesListView


urlpatterns = [
    url(r'^(?P<slug>[\w_-]+)/?$', ItemPageView.as_view(), {'items': Game}, name='item_details'),
    url(r'^/?$', GamesListView.as_view(), name='games_list'),
]
