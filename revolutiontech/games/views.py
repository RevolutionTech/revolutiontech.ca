"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

from basecategory.views import CategoryPageView


class GamesListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(GamesListView, self).get_context_data(**kwargs)
        context['page'] = 'games'
        return context
