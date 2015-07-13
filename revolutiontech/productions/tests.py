"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.test import TestCase

from productions.models import ProductionCategory, Production


class ProductionsTestCase(TestCase):

    def setUp(self):
        self.category = ProductionCategory.objects.create(name='Main cat')

    def tearDown(self):
        ProductionCategory.objects.all().delete()

    def testCreateProduction(self):
        production_name = 'Production ABC'
        production = Production.objects.create(name=production_name, category=self.category)
        self.assertEquals(unicode(production), production_name)
