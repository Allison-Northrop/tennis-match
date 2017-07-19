from django.db import models
from django.utils import timezone

# Create your models here.
class Player_Attributes(models.Model):
    username = models.CharField(max_length=100)
    skill_level = models.FloatField()
    address = models.CharField(max_length=500)
    availability_days = models.CharField(max_length=500)
    availability_times = models.CharField(max_length=500)
    looking_for = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    additional_info = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)


        # def geocoder
