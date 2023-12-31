from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexPage.as_view(), name='home'),
    path('review', views.see_reviews, name='review'),
    path('submit_review', views.submit_review, name='submit_review'),
    path('view_booking', views.view_booking, name='view_booking'),
    path('add_booking', views.add_booking, name='add_booking'),
    path('edit/<booking_id>', views.edit_booking, name='edit_booking'),
    path('delete/<booking_id>', views.delete_booking, name='delete_booking'),
    path('contact', views.ContactUs.as_view(), name='contact'),
]
