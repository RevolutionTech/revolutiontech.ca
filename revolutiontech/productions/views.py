"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

from basecategory.views import CategoryPageView


class ProductionsListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(ProductionsListView, self).get_context_data(**kwargs)
        context['page'] = 'productions'
        return context
