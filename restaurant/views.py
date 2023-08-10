from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm


# Create your views here.
class BookTable(FormView):
    form_class = BookingForm
    template_name = "index.html"
