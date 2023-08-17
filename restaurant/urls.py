from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('booking', views.BookTable.as_view(), name='booking'),
    path('review', views.LeaveReview.as_view(), name='review'),
]