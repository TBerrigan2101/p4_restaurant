from django import forms
from .models import Booking, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'guests', 'message', )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'body', )
