"""
:Created: 17 July 2015
:Author: Lucas Connors

"""

from basecategory.views import CategoryPageView

from games.models import Game


class GamesListView(CategoryPageView):

    def get_context_data(self, **kwargs):
        context = super(GamesListView, self).get_context_data(**kwargs)
        context['page'] = 'games'

        games = Game.objects.all().order_by('name')
        context['items'] = {
            'heroes': games.filter(hero=True),
            'regular': games.filter(hero=False),
        }
        return context
