from rest_framework.test import APIClient
from organization.tests import base_test


class UserLoginTestCase(base_test.NewUserTestCase):
    """
    This class is used to test the login functionality and
    check whether a user is successfully getting logged in to the
    system.
    """

    def setUp(self) -> None:
        super().setUp()

    def test_user_login(self):
        client = APIClient()
        result = client.post('/api/v1/user/api/token/', {'username': self.username,
                                                     'password': self.password},
                             format='json')

        self.assertEquals(result.status_code, 200)
        self.assertTrue('access' in result.json())
        self.assertTrue('refresh' in result.json())

    def tearDown(self) -> None:
        self.client.logout()
        super().tearDown()