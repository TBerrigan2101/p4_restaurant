from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookTable.as_view(), name='home'),
]