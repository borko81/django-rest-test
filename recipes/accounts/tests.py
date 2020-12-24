from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import SignUpView


class TestUrlAccount(SimpleTestCase):
    def test_signup_is_resolve(self):
        url = reverse('sign_up')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, SignUpView)
