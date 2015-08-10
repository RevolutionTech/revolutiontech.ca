"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

import random

from basecategory.views import CategoryPageView
from games.models import GameCategory, Game


class GamesListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(GamesListView, self).get_context_data(**kwargs)
        context['page'] = 'games'

        games = Game.objects.filter(visible=True).order_by('name')
        heroes = games.filter(hero=True)
        regular = games.filter(hero=False)
        context['items'] = {
            'heroes': heroes,
            'regular': regular,
        }
        context['random_hero_unit_index'] = random.randint(0, heroes.count()-1) if heroes.count() > 0 else 0

        regular_categories = regular.values('category')
        category_ids = set(map(lambda cat: cat['category'], regular_categories))
        context['categories'] = GameCategory.objects.filter(id__in=category_ids).order_by('name')

        return context
