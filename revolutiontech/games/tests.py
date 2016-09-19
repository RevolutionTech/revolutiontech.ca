"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase, MigrationTestCase


class GamesInitialOrdersMigrationTestCase(MigrationTestCase):

    migrate_from = '0004_game_visible'
    migrate_to = '0006_auto_20160919_0008'

    def setUpBeforeMigration(self, apps):
        # Create a game category
        GameCategory = apps.get_model('games', 'GameCategory')
        self.premigration_game_category = GameCategory.objects.create(name='Action')

        # Create a game
        Game = apps.get_model('games', 'Game')
        self.premigration_game = Game.objects.create(
            name='Acid Drop',
            slug='acid-drop',
            category=self.premigration_game_category
        )

    def testInstancesHaveInitialOrder(self):
        GameCategory = self.apps.get_model('games', 'GameCategory')
        game_category = GameCategory.objects.get(id=self.premigration_game_category.id)
        self.assertEquals(game_category.order, game_category.id)

        Game = self.apps.get_model('games', 'Game')
        game = Game.objects.get(id=self.premigration_game.id)
        self.assertEquals(game.order, game.id)


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
