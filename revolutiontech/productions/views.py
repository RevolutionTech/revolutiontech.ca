"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

from basecategory.views import CategoryPageView

from productions.models import ProductionCategory, Production


class ProductionsListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(ProductionsListView, self).get_context_data(**kwargs)
        context['page'] = 'productions'

        productions = Production.objects.all().order_by('name')
        heroes = productions.filter(hero=True)
        regular = productions.filter(hero=False)
        context['items'] = {
            'heroes': heroes,
            'regular': regular,
        }

        regular_categories = regular.values('category')
        category_ids = set(map(lambda cat: cat['category'], regular_categories))
        context['categories'] = ProductionCategory.objects.filter(id__in=category_ids).order_by('name')

        return context
