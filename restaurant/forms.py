from django import forms
from .models import Booking, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'guests', 'message', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'guests': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'title', 'body', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),

        }

