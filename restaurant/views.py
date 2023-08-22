from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking, Review, Menu
from .forms import BookingForm, ReviewForm


# Create your views here.


def view_booking(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
        }
    return render(request, 'view_booking.html', context)


def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'add_booking.html', context)  


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('view_booking')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('view_booking')


class MenuList(generic.ListView):
    model = Menu
    queryset = Menu.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 6


class IndexPage(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'index.html'


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

