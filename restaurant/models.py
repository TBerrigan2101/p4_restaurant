from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.TextField()
    guests = models.IntegerField(default='')
    message= models.TextField()


    def __str__(self):
     return self.name


class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"