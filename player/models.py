from django.db import models
from django.utils import timezone

# Create your models here.
class Player_Attributes(models.Model):
    username = models.CharField(max_length=100)
    skill_level = models.DecimalField(..., max_digits=2, decimal_places=2)
    address = models.CharField(max_length=500)
    availability_days = models.CharField(max_length=500)
    availability_times = models.CharField(max_length=500)
    looking_for = models.CharField(max_length=500)
    contact_info = models.CharField(max_length=11)
    additional_info = models.TextField()
