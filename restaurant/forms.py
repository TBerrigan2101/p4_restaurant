from django import forms
from .models import Booking, Review, Contact

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'date', 'time', 'email', 'phone', 'guests', 'message', )
        widgets = {
            'date': DateInput()
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message', )