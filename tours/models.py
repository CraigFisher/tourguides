from django.db import models
from profiles.models import GuideProfile
from cities_light.models import Country, Region, City


class Tour(models.Model):
    tour_guide = models.ForeignKey(GuideProfile)

    name = models.CharField(max_length=300)
    overview = models.TextField(null=True)
    itinerary = models.TextField(null=True)
    max_seating = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    country = models.ForeignKey(Country)
    city = models.ForeignKey(City, null=True)
    region = models.ForeignKey(Region, null=True)

    start_time = models.TimeField()
    end_time = models.TimeField()
