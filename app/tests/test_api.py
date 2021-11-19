from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UserAuthenticationTest(APITestCase):
    sign_up_url = reverse("app:signup")


    def test_user_sign_up(self):
        data = {
            'username':'stark',
            'password': 'testing321'
        }
        res = self.client.post(self.sign_up_url,data = data)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        self.assertEqual(res.json()['status'],'success')
