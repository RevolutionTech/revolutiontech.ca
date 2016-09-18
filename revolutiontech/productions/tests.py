"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase


class ProductionsTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/productions/',
            '/productions/{slug}/'.format(slug=self.production.slug),
        ]
