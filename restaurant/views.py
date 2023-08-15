from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm


# Create your views here.


class BookTable(CreateView):
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = '/'



class LeaveReview():
    template_name = "review.html"
