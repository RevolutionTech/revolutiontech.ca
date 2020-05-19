"""
:Created: 12 July 2015
:Author: Lucas Connors

"""

from revolutiontech.tests import MigrationTestCase, RevolutionTechTestCase


class ProductionsInitialOrdersMigrationTestCase(MigrationTestCase):

    migrate_from = "0004_production_visible"
    migrate_to = "0006_auto_20160919_0008"

    def setUpBeforeMigration(self, apps):
        # Create a production category
        ProductionCategory = apps.get_model("productions", "ProductionCategory")
        self.premigration_production_category = ProductionCategory.objects.create(
            name="Animation"
        )

        # Create a production
        Production = apps.get_model("productions", "Production")
        self.premigration_production = Production.objects.create(
            name="Connect",
            slug="connect",
            category=self.premigration_production_category,
        )

    def testInstancesHaveInitialOrder(self):
        ProductionCategory = self.apps.get_model("productions", "ProductionCategory")
        production_category = ProductionCategory.objects.get(
            id=self.premigration_production_category.id
        )
        self.assertEqual(production_category.order, production_category.id)

        Production = self.apps.get_model("productions", "Production")
        production = Production.objects.get(id=self.premigration_production.id)
        self.assertEqual(production.order, production.id)


class ProductionsAdminWebTestCase(RevolutionTechTestCase):
    def get200s(self):
        return [
            "/admin/productions/",
            "/admin/productions/productioncategory/",
            "/admin/productions/productioncategory/add/",
            "/admin/productions/productioncategory/{category_id}/change/".format(
                category_id=self.production_category.id
            ),
            "/admin/productions/production/",
            "/admin/productions/production/add/",
            "/admin/productions/production/{production_id}/change/".format(
                production_id=self.production.id
            ),
        ]


class ProductionsWebTestCase(RevolutionTechTestCase):
    def get200s(self):
        return ["/productions/", f"/productions/{self.production.slug}/"]
