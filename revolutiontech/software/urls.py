"""
:Created: 26 July 2015
:Author: Lucas Connors

"""

from django.conf.urls import url

from basecategory.views import ItemPageView
from software.models import Software
from software.views import SoftwareListView


urlpatterns = [
    url(r'^(?P<slug>[\w_-]+)/?$', ItemPageView.as_view(), {'items': Software}, name='item_details'),
    url(r'^/?$', SoftwareListView.as_view(), name='software_list'),
]
