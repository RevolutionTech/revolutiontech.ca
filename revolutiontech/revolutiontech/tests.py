"""
:Created: 18 September 2016
:Author: Lucas Connors

"""

from django.apps import apps
from django.contrib.auth.models import User
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.test import TestCase
from django.utils.text import slugify

from pigeon.test import RenderTestCase

from basecategory.models import Platform
from games.models import GameCategory, Game, GameVideo
from productions.models import ProductionCategory, Production
from software.models import Software, SoftwareButton


class RevolutionTechTestCase(RenderTestCase):

    USER_USERNAME = 'jsmith'
    USER_EMAIL = 'jsmith@example.com'
    USER_PASSWORD = 'abc123'

    PLATFORM_NAME = 'Windows'
    GAME_CATEGORY_NAME = 'Puzzle'
    GAME_NAME = 'Blockade'
    PRODUCTION_CATEGORY_NAME = 'Videography'
    PRODUCTION_NAME = 'The Gum Thief'
    SOFTWARE_NAME = 'Flamingo'

    def setUp(self):
        super(RevolutionTechTestCase, self).setUp()

        # Create admin user
        self.user = User.objects.create_user(self.USER_USERNAME, email=self.USER_EMAIL, password=self.USER_PASSWORD)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username=self.USER_USERNAME, password=self.USER_PASSWORD)

        # Create initial item instances
        self.platform = Platform.objects.create(name=self.PLATFORM_NAME, css_class=self.PLATFORM_NAME.lower())
        self.game_category = GameCategory.objects.create(name=self.GAME_CATEGORY_NAME)
        self.production_category = ProductionCategory.objects.create(name=self.PRODUCTION_CATEGORY_NAME)
        self.game = Game.objects.create(
            name=self.GAME_NAME,
            slug=slugify(self.GAME_NAME),
            description="The idea of <em>Blockade</em> spawned from the basic mechanics of <em>Tetris</em>.",
            hero=True,
            category=self.game_category
        )
        self.production = Production.objects.create(
            name=self.PRODUCTION_NAME,
            slug=slugify(self.PRODUCTION_NAME),
            category=self.production_category
        )
        self.software = Software.objects.create(name=self.SOFTWARE_NAME, slug=slugify(self.SOFTWARE_NAME))

        # Create instances attached to items
        GameVideo.objects.create(
            game=self.game,
            title='Blockade Trailer',
            youtube_url='http://www.youtube.com/watch?v=1lAI5e-zkxA&t=1s'
        )
        SoftwareButton.objects.create(software=self.software, text='View Site', external_url='http://flamingo.photo/')


class MigrationTestCase(TestCase):
    """
    Ref: https://www.caktusgroup.com/blog/2016/02/02/writing-unit-tests-django-migrations/
    """

    migrate_from = None
    migrate_to = None

    @property
    def app(self):
        return apps.get_containing_app_config(type(self).__module__).name

    def setUp(self):
        # Verify that migration_from and migration_to are defined
        assertion_error_message = (
            "MigrationTestCase '{test_case_name}' must define migrate_from and migrate_to properties."
        ).format(test_case_name=type(self).__name__)
        assert self.migrate_from and self.migrate_to, assertion_error_message

        # Init MigrationExecutor
        self.migrate_from = [(self.app, self.migrate_from)]
        self.migrate_to = [(self.app, self.migrate_to)]
        executor = MigrationExecutor(connection)
        old_apps = executor.loader.project_state(self.migrate_from).apps

        # Reverse to old migration
        executor.migrate(self.migrate_from)

        # Create model instances before migration runs
        self.setUpBeforeMigration(old_apps)

        # Run the migration to test
        executor = MigrationExecutor(connection)
        executor.loader.build_graph()
        executor.migrate(self.migrate_to)
        self.apps = executor.loader.project_state(self.migrate_to).apps

    def setUpBeforeMigration(self, apps):
        pass


class AdminWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/admin/',
        ]

    def testAdminLoginPageRenders(self):
        self.client.logout()
        self.assertResponseRedirects('/admin/', '/admin/login/')
