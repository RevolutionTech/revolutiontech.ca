"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from games.models import Game
from revolutiontech.tests import RevolutionTechTestCase


class GamesTestCase(RevolutionTechTestCase):

    def testCreateGame(self):
        game_name = 'Game ABC'
        game = Game.objects.create(name=game_name, category=self.game_category)
        self.assertEquals(unicode(game), game_name)
