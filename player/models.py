from django.db import models
from django.utils import timezone
import urllib.request
import json
from decimal import Decimal
from django.contrib.auth.models import User

# Create your models here.
class Player_Attributes(models.Model):
    username = models.ForeignKey(User)
    skill_level = models.FloatField()
    address = models.CharField(max_length=500)
    availability_days = models.CharField(max_length=500)
    availability_times = models.CharField(max_length=500)
    looking_for = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    additional_info = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0, null=True)

    def save(self):
        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = self.geocode(self.address)

        super(Player_Attributes, self).save()

    def geocode(self, address):
        address = urllib.parse.quote_plus(address)
        maps_api_url = "?".join([
            "http://maps.googleapis.com/maps/api/geocode/json",
            urllib.parse.urlencode({"address": address, "sensor": False})
        ])
        response = urllib.request.urlopen(maps_api_url)
        data = json.loads(response.read().decode('utf8'))

        if data['status'] == 'OK':
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            return Decimal(latitude), Decimal(longitude)
