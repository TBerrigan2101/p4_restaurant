from django.test import TestCase
from .forms import BookingForm, ReviewForm, ContactForm

# Create your tests here.


# Booking Form Tests

class TestBookingForm(TestCase):

    def test_item_name_is_required(self):
        form = BookingForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_item_date_is_required(self):
        form = BookingForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_item_time_is_required(self):
        form = BookingForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_item_email_is_required(self):
        form = BookingForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_item_phone_is_required(self):
        form = BookingForm({'phone': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors.keys())
        self.assertEqual(form.errors['phone'][0], 'This field is required.')

    def test_item_guests_is_required(self):
        form = BookingForm({'guests': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('guests', form.errors.keys())
        self.assertEqual(form.errors['guests'][0], 'This field is required.')

    def test_item_message_is_required(self):
        form = BookingForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ('name', 'date', 'time', 'email', 'phone', 'guests', 'message'))


# Review Form Tests

class TestReviewForm(TestCase):

    def test_review_name_is_required(self):
        form = ReviewForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_review_body_is_required(self):
        form = ReviewForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ('name', 'body'))


# Contact Form Tests

class TestContactForm(TestCase):

    def test_contact_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_contact_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_contact_subject_is_required(self):
        form = ContactForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')

    def test_contact_message_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields, ('name', 'email', 'subject', 'message'))
