"""
:Created: 18 September 2016
:Author: Lucas Connors

"""

from django.test import TestCase

from games.models import GameCategory
from productions.models import ProductionCategory


class RevolutionTechTestCase(TestCase):

    GAME_CATEGORY_NAME = 'Action'
    PRODUCTION_CATEGORY_NAME = 'Videography'

    def setUp(self):
        super(RevolutionTechTestCase, self).setUp()

        # Create initial instances
        self.game_category = GameCategory.objects.create(name=self.GAME_CATEGORY_NAME)
        self.production_category = ProductionCategory.objects.create(name=self.PRODUCTION_CATEGORY_NAME)
