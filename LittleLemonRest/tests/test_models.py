from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuTest(TestCase):

    def test_get_items(self):
        item = Menu.objects.create(title='Ice cream', price=80, inventory=100)
        self.assertEquals(str(item), "Ice cream : 80")