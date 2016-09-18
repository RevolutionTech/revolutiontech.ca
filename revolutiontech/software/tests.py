"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase


class SoftwareTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/software/',
            '/software/{slug}/'.format(slug=self.software.slug),
        ]
