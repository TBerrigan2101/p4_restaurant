from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking, Review, Contact
from .forms import BookingForm, ReviewForm, ContactForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# <----- Index Views. Contact was originally on the page but it looked too busy. This view is to keep the page rendering ----->

class IndexPage(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'index.html'


# <----- Review Views ----->

def see_reviews(request):
    reviews = Review.objects.filter(approved=True).order_by("-created_on")
    context = {
        'reviews': reviews
        }
    return render(request, 'review.html', context)


@login_required(login_url="accounts/login")
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.created_by = request.user
            review.save()
            return redirect('review')
    form = ReviewForm()
    context = {
        'review_form': form
    }
    return render(request, 'submit_review.html', context)


# <----- Booking Views ----->

@login_required(login_url="accounts/login")
def view_booking(request):
    bookings = Booking.objects.filter(created_by=request.user)
    context = {
        'bookings': bookings
        }
    return render(request, 'view_booking.html', context)


def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.created_by = request.user
            booking.save()
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


# <----- Contact Views ----->

class ContactUs(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'
