from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Snack


class SnackPageTests(TestCase):
     def setUp(self):
        # Create a test user
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a snack object for testing
        self.snack = Snack.objects.create(
            name='Test Snack',
            purchaser=self.user,
            description='Test snack description'
        )
     def test_snack_list_page(self):
        # Generate the URL for the snack list page
        url = reverse('snack_list')

        # Make a GET request to the URL
        response = self.client.get(url)

        # Verify the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify the template used is 'snack_list.html'
        self.assertTemplateUsed(response, 'snack_list.html')

     def test_snack_detail_page(self):
        # Generate the URL for the snack detail page using the snack's ID
        url = reverse('snack_detail', args=[self.snack.pk])

        # Make a GET request to the URL
        response = self.client.get(url)

        # Verify the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verify the template used is 'snack_detail.html'
        self.assertTemplateUsed(response, 'snack_detail.html')

        # Verify the content of the response
        self.assertContains(response, self.snack.name)
        self.assertContains(response, self.snack.description)
        self.assertContains(response, self.snack.purchaser.username)


