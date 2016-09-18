"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase


class GamesAdminWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/admin/games/',
            '/admin/games/gamecategory/',
            '/admin/games/gamecategory/add/',
            '/admin/games/gamecategory/{category_id}/change/'.format(category_id=self.game_category.id),
            '/admin/games/game/',
            '/admin/games/game/add/',
            '/admin/games/game/{game_id}/change/'.format(game_id=self.game.id),
        ]


class GamesWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/games/',
            '/games/{slug}/'.format(slug=self.game.slug),
        ]
