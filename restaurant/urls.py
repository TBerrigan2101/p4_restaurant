from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('booking', views.BookTable.as_view(), name='booking'),
]