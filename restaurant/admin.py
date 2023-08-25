from django.contrib import admin
from .models import Booking, Review, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'email', 'phone', 'guests', 'message')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_by')
    list_display = ('name', 'body', 'created_by')
    list_display_links = ('name', 'body', 'created_by')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
