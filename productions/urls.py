"""
:Created: 26 July 2015
:Author: Lucas Connors

"""

from django.conf.urls import url

from basecategory.views import ItemPageView
from productions.models import Production
from productions.views import ProductionsListView


app_name = 'productions'
urlpatterns = [
    url(r'^(?P<slug>[\w_-]+)/?$', ItemPageView.as_view(), {'items': Production}, name='item_details'),
    url(r'^$', ProductionsListView.as_view(), {'items': Production}, name='productions_list'),
]
