"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from django.test import TestCase

from software.models import Software


class SoftwareTestCase(TestCase):

    def testCreateSoftware(self):
        software_name = 'Software ABC'
        software = Software.objects.create(name=software_name)
        self.assertEquals(unicode(software), software_name)
