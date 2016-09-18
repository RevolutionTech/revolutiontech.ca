"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase


class GamesWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/games/',
            '/games/{slug}/'.format(slug=self.game.slug),
        ]
