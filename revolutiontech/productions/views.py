"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

import random

from basecategory.views import CategoryPageView
from productions.models import ProductionCategory, Production


class ProductionsListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(ProductionsListView, self).get_context_data(**kwargs)
        context['page'] = 'productions'

        productions = Production.objects.filter(visible=True).order_by('name')
        heroes = productions.filter(hero=True)
        regular = productions.filter(hero=False)
        context['items'] = {
            'heroes': heroes,
            'regular': regular,
        }
        context['random_hero_unit_index'] = random.randint(0, heroes.count()-1) if heroes.count() > 0 else 0

        regular_categories = regular.values('category')
        category_ids = set(map(lambda cat: cat['category'], regular_categories))
        context['categories'] = ProductionCategory.objects.filter(id__in=category_ids).order_by('name')

        return context
