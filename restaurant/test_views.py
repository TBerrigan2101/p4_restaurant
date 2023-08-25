from django.test import TestCase
from django.urls import reverse
from .models import Booking, Contact, Review


# WORKING
class TestIndexView(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestBookingViews(TestCase):

    # def test_view_booking(self):
    #     response = self.client.get(reverse('view_booking'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'view_booking.html')

# WORKING
    def test_add_booking(self):
        response = self.client.get(reverse('add_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_booking.html')

# WORKING
    def test_edit_booking(self):
        booking = Booking.objects.create(name='Test Booking')
        response = self.client.get(f'/edit/{booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html')

    def test_delete_booking(self):
        booking = Booking.objects.create(name='Delete Booking')
        response = self.client.get(f'/delete/{booking.id}')
        self.assertRedirects(response, 'view_booking')
        existing_items = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(existing_items), 0)


# WORKING
class TestReviewViews(TestCase):

    def test_see_reviews(self):
        response = self.client.get(reverse('review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')

# WORKING IF @LOGIN REQUIRED IS REMOVED
    def test_submit_review(self):
        response = self.client.get(reverse('submit_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_review.html')


# WORKING
class TestContactViews(TestCase):

    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
