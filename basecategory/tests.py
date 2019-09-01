"""
:Created: 18 September 2016
:Author: Lucas Connors

"""

from revolutiontech.tests import RevolutionTechTestCase


class BaseCategoryAdminWebTestCase(RevolutionTechTestCase):
    def get200s(self):
        return [
            "/admin/basecategory/",
            "/admin/basecategory/platform/",
            "/admin/basecategory/platform/add/",
            "/admin/basecategory/platform/{platform_id}/change/".format(
                platform_id=self.platform.id
            ),
        ]


class HomeWebTestCase(RevolutionTechTestCase):
    def get200s(self):
        return ["/"]
