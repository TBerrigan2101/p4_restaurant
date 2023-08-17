from django.contrib import admin
from .models import Booking, Review, Menu
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'email', 'phone', 'guests', 'message')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_on')
    list_display = ('name', 'email', 'body', 'created_on',)
