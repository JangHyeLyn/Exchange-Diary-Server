import jwt
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from Accounts.models import User


class UserTest(APITestCase):
    def setUp(self) -> None:
        User.objects.create(
            email='testuser@test.com',
            password='testuser',
            username='testuser',
            description='test_description',
        )
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        test_user = User.objects.get(email='testuser@test.com')
        payload = jwt_payload_handler(test_user)
        self.token = jwt_encode_handler(payload)

    # api/v1/user/me/
    def test_api_v1_user_me(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        token = header['HTTP_AUTHORIZATION']

        payload = api_settings.JWT_DECODE_HANDLER(token)
        user_id = api_settings.JWT_PAYLOAD_GET_USER_ID_HANDLER(payload)
        user_name = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER(payload)
        self.client.credentials(HTTP_AUTHORIZATION=f'jwt {header.get("HTTP_AUTHORIZATION")}')

        response = self.client.get('/api/v1/users/me/', data={'format': 'json'})
        # check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # check user_id
        self.assertEqual(response.data.get('id'), user_id)
        # check user_name
        self.assertEqual(response.data.get('username'), user_name)
        # check user_description
        self.assertEqual(response.data.get('description'), User.objects.get(pk=user_id).description)
