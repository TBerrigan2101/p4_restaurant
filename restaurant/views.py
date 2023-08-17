from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking, Review, Menu
from .forms import BookingForm, ReviewForm


# Create your views here.

class MenuList(generic.ListView):
    model = Menu
    queryset = Menu.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class IndexPage(CreateView):
    model = Booking
    form_class = BookingForm
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
