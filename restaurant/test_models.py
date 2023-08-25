from django.test import TestCase
from .models import Booking, Review, Contact

# Create your tests here.


# Working
class TestBookingModel(TestCase):

    def test_name_string_method_returns_phone(self):
        booking = Booking.objects.create(phone='123')
        self.assertEqual(str(booking.phone), '123')

    def test_name_string_method_returns_name(self):
        booking = Booking.objects.create(name='Test Booking Name')
        self.assertEqual(str(booking.name), 'Test Booking Name')


# Working
class TestContactModel(TestCase):

    def test_name_string_method_returns_name(self):
        contact = Contact.objects.create(name='Test Contact Name')
        self.assertEqual(str(contact.name), 'Test Contact Name')


# Working
class TestReviewModel(TestCase):

    def test_review_approval_defaults_false(self):
        review = Review.objects.create(name='Test Review Item')
        self.assertFalse(review.approved)
