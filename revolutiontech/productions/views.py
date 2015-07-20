"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

from basecategory.views import CategoryPageView

from productions.models import Production


class ProductionsListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(ProductionsListView, self).get_context_data(**kwargs)
        context['page'] = 'productions'

        productions = Production.objects.all().order_by('name')
        context['items'] = {
            'heroes': productions.filter(hero=True),
            'regular': productions.filter(hero=False),
        }
        return context
