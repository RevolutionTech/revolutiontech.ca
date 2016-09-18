"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase
from software.models import Software


class SoftwareTestCase(RevolutionTechTestCase):

    def testCreateSoftware(self):
        software_name = 'Software ABC'
        software = Software.objects.create(name=software_name)
        self.assertEquals(unicode(software), software_name)
