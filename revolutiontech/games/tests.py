"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.test import TestCase

from games.models import GameCategory, Game


class GamesTestCase(TestCase):

    def setUp(self):
        self.category = GameCategory.objects.create(name='Main cat')

    def tearDown(self):
        GameCategory.objects.all().delete()

    def testCreateGame(self):
        game_name = 'Game ABC'
        game = Game.objects.create(name=game_name, category=self.category)
        self.assertEquals(unicode(game), game_name)
