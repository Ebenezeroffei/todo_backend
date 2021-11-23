from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

class UserAuthenticationTest(APITestCase):
    sign_up_url = reverse("app:signup")
    sign_in_url = reverse('app:signin')

    def test_user_sign_up(self):
        data = {
            'username':'stark',
            'email': 'stark@gmail.com',
            'password': 'testing321'
        }
        res = self.client.post(self.sign_up_url,data = data)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        self.assertEqual(res.json()['status'],'success')

    def test_user_sign_in(self):
        # Sign up user
        data = {
            'username':'stark',
            'email': 'stark@gmail.com',
            'password': 'testing321'
        }
        res = self.client.post(self.sign_up_url,data = data)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        self.assertEqual(res.json()['status'],'success')
        # Sign in user
        res = self.client.post(self.sign_in_url,data = data)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.json()['status'],'success')

        


class PasswordReset(APITestCase):
    password_reset_url = reverse('password_reset:reset-password-request')

    def setUp(self) -> None:
        user = User(
            username = 'stark',
            email = 'stark@gmail.com'
        )
        user.set_password('testing321')
        user.save()


    def test_password_reset(self):
        data = {'email':'stark@gmail.com'}
        res = self.client.post(self.password_reset_url,data=data)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.json()['status'],"OK")
