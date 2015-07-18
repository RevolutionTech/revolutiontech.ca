"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

from basecategory.views import CategoryPageView


class SoftwareListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(SoftwareListView, self).get_context_data(**kwargs)
        context['page'] = 'software'
        return context
