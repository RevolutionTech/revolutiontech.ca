"""
:Created: 18 September 2016
:Author: Lucas Connors

"""

from django.contrib.auth.models import User
from django.test import TestCase

from games.models import GameCategory
from productions.models import ProductionCategory


class RevolutionTechTestCase(TestCase):

    USER_USERNAME = 'jsmith'
    USER_EMAIL = 'jsmith@example.com'
    USER_PASSWORD = 'abc123'

    GAME_CATEGORY_NAME = 'Action'
    PRODUCTION_CATEGORY_NAME = 'Videography'

    @staticmethod
    def strip_query_params(url):
        return url.split('?')[0]

    def assertResponseRenders(self, url, status_code=200, method='GET', data={}, has_form_error=False, **kwargs):
        request_method = getattr(self.client, method.lower())
        follow = status_code == 302
        response = request_method(url, data=data, follow=follow, **kwargs)

        if status_code == 302:
            redirect_url, response_status_code = response.redirect_chain[0]
        else:
            response_status_code = response.status_code
        self.assertEquals(
            response_status_code,
            status_code,
            "URL {url} returned with status code {actual_status} when {expected_status} was expected.".format(
                url=url,
                actual_status=response_status_code,
                expected_status=status_code
            )
        )

        # Check that forms submitted did not return errors (or did if it should have)
        form_error_assertion_method = self.assertIn if has_form_error else self.assertNotIn
        form_error_assertion_method('errorlist', response.content)

        return response

    def assertResponseRedirects(self, url, redirect_url, method='GET', data={}, **kwargs):
        response = self.assertResponseRenders(url, status_code=302, method=method, data=data, **kwargs)
        redirect_url_from_response, _ = response.redirect_chain[0]
        self.assertEquals(self.strip_query_params(redirect_url_from_response), redirect_url)
        self.assertEquals(response.status_code, 200)

    def get200s(self):
        return []

    def setUp(self):
        super(RevolutionTechTestCase, self).setUp()

        # Create admin user
        self.user = User.objects.create_user(self.USER_USERNAME, email=self.USER_EMAIL, password=self.USER_PASSWORD)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username=self.USER_USERNAME, password=self.USER_PASSWORD)

        # Create initial instances
        self.game_category = GameCategory.objects.create(name=self.GAME_CATEGORY_NAME)
        self.production_category = ProductionCategory.objects.create(name=self.PRODUCTION_CATEGORY_NAME)

    def testRender200s(self):
        for url in self.get200s():
            self.assertResponseRenders(url)


class AdminWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/admin/',
        ]

    def testAdminLoginPageRenders(self):
        self.client.logout()
        self.assertResponseRedirects('/admin/', '/admin/login/')


class HomeWebTestCase(RevolutionTechTestCase):

    def get200s(self):
        return [
            '/',
        ]