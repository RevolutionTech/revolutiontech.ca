"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

import random

from basecategory.views import CategoryPageView
from software.models import Software


class SoftwareListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(SoftwareListView, self).get_context_data(**kwargs)
        context['page'] = 'software'

        software = Software.objects.filter(visible=True).order_by('name')
        heroes = software.filter(hero=True)
        regular = software.filter(hero=False)
        context['items'] = {
            'heroes': heroes,
            'regular': regular,
        }
        context['random_hero_unit_index'] = random.randint(0, heroes.count()-1) if heroes.count() > 0 else 0
        return context
