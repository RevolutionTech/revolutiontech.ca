"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase


class SoftwareAdminWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/admin/software/',
            '/admin/software/software/',
            '/admin/software/software/add/',
            '/admin/software/software/{software_id}/change/'.format(software_id=self.software.id),
        ]


class SoftwareWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/software/',
            '/software/{slug}/'.format(slug=self.software.slug),
        ]
