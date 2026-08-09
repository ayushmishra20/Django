from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LogoutViewTests(TestCase):
    def test_logout_view_logs_out_authenticated_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='logoutuser',
            email='logout@example.com',
            password='secret123'
        )

        self.client.force_login(user)

        response = self.client.post(reverse('logout'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have been logged out')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
