from django.db import models
from profiles.models import MemberProfile
from tours.models import Tour


class Booking(models.Model):
    member = models.ForeignKey(MemberProfile)
    tour = models.ForeignKey(Tour)

    number_guests = models.SmallIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    STATUS_TYPES = (
                    ('req', 'REQUESTED'),
                    ('conf', 'CONFIRMED'),
                    ('prog', 'IN_PROGRESS'),
                    ('fin', 'FINISHED'),
                    ('canc', 'CANCELLED'),
                   )
    status = models.CharField(max_length=4, choices=STATUS_TYPES,
                              default='R')
    request_time = models.DateTimeField()
    cancelation_time = models.DateTimeField(null=True)
    confirmation_time = models.DateTimeField(null=True)
