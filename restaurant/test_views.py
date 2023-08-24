from django.test import TestCase
from django.urls import reverse
from .models import Booking, Contact, Review


class TestBookingViews(TestCase):

#     def test_view_booking(self):
#         response = self.client.get(reverse('view_booking'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'view_booking.html')

    def test_add_booking(self):
        response = self.client.get(reverse('add_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_booking.html')

    # def test_edit_booking(self):
    #     response = self.client.get(reverse('edit_booking'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'edit_booking.html')


class TestContactViews(TestCase):

    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


class TestReviewViews(TestCase):

    def test_submit_review(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')