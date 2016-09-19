"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase, MigrationTestCase


class SoftwareInitialOrdersMigrationTestCase(MigrationTestCase):

    migrate_from = '0004_software_visible'
    migrate_to = '0006_auto_20160919_0008'

    def setUpBeforeMigration(self, apps):
        # Create software
        Software = apps.get_model('software', 'Software')
        self.premigration_software = Software.objects.create(name='Seared Quail', slug='seared-quail')

    def testInstancesHaveInitialOrder(self):
        Software = self.apps.get_model('software', 'Software')
        software = Software.objects.get(id=self.premigration_software.id)
        self.assertEquals(software.order, software.id)


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
