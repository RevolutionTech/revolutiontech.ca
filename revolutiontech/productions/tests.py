"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase


class ProductionsAdminWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/admin/productions/',
            '/admin/productions/productioncategory/',
            '/admin/productions/productioncategory/add/',
            '/admin/productions/productioncategory/{category_id}/change/'.format(
                category_id=self.production_category.id
            ),
            '/admin/productions/production/',
            '/admin/productions/production/add/',
            '/admin/productions/production/{production_id}/change/'.format(production_id=self.production.id),
        ]


class ProductionsWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/productions/',
            '/productions/{slug}/'.format(slug=self.production.slug),
        ]
