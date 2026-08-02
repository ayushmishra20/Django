from django.test import TestCase


class LogoutPageTests(TestCase):
    def test_logout_page_renders_for_get_request(self):
        response = self.client.get('/logout/', HTTP_HOST='localhost')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have been logged out')
