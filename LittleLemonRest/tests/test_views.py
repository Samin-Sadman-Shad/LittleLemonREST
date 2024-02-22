from django.contrib.auth.models import User
from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer
from restaurant import views
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Sadman", password="sadman123")
        self.token = Token.objects.create(user=self.user)

        item1 = Menu.objects.create(title='Fruit cake', price=60, inventory=100)
        item2 = Menu.objects.create(title='Chicken soup', price=10, inventory=50)

    def test_getAll(self):
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)

        apiClient = APIClient()
        apiClient.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        url = reverse('menu')

        response = apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serialized.data)