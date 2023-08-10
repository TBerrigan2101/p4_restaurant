from django.contrib import admin
from .models import Booking, Review

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('name', 'guests')
    list_display = ('name', 'email', 'phone', 'guests', 'message')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_on')
    list_display = ('name', 'email', 'body', 'created_on',)