from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Booking, Review
from .forms import BookingForm, ReviewForm


# Create your views here.
class IndexPage(CreateView):
    model = Booking
    template_name = 'index.html'


class BookTable(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = '/'


class LeaveReview(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review.html'
    success_url = '/'
    
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "review.html",
            {
                "review_form": ReviewForm()
            },
        )

