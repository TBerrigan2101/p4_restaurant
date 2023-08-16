from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm, ReviewForm


# Create your views here.
class IndexPage(ListView):
    model = Booking
    template_name = 'index.html'


class BookTable(CreateView):
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = '/'


class LeaveReview(CreateView):
    form_class = ReviewForm
    template_name = 'review.html'
    success_url = '/'

