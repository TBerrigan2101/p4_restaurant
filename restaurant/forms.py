from django import forms
from .models import Booking, Review

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'date', 'email', 'phone', 'guests', 'message', )
        widgets = {
            'date': DateInput()
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', )
