"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from productions.models import Production
from revolutiontech.tests import RevolutionTechTestCase


class ProductionsTestCase(RevolutionTechTestCase):

    def testCreateProduction(self):
        production_name = 'Production ABC'
        production = Production.objects.create(name=production_name, category=self.production_category)
        self.assertEquals(unicode(production), production_name)
