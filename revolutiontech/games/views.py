"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

from basecategory.views import CategoryPageView
from games.models import GameCategory


class GamesListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(GamesListView, self).get_context_data(**kwargs)
        regular = context['items']['regular']

        regular_categories = regular.values('category')
        category_ids = set(map(lambda cat: cat['category'], regular_categories))
        context['categories'] = GameCategory.objects.filter(id__in=category_ids).order_by('order')

        return context
