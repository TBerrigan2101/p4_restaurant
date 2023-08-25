from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

# <----- Booking Models ----->

TIMES = (
    ("3:00 PM", "3:00 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4:00 PM", "4:00 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5:00 PM", "5:00 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6:00 PM", "6:00 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7:00 PM", "7:00 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8:00 PM", "8:00 PM"),
    ("8:30 PM", "8:30 PM"),
    ("9:00 PM", "9:00 PM"),
    ("9:30 PM", "9:30 PM"),

)


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    guests = models.IntegerField(default='1')
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIMES, default="3 PM")
    message = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


# <----- Review Models ----->

class Review(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"


# <----- Contact Models ----->

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
