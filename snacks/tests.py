from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


# Create your tests here.
class SnacksTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='test',
            email='teas@email.com',
            password='1234'
        )

        self.snack = Snack.objects.create(
            title='test',
            description="test info",
            purchaser = self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),"test")

    def test_detail_view(self):
        url = reverse('snack_details', args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_details.html')

    def test_create_view(self):
        obj={
            'title':"test2",
            'description': "info...",
            'purchaser': self.user.id
        }

        url = reverse('snack_create')
        response = self.client.post(path=url,data=obj,follow=True)
        # self.assertEqual(len(Thing.objects.all()),2)
        self.assertRedirects(response, reverse('snack_details', args=[2]))