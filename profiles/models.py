from django.db import models
from django.contrib.auth.models import User
from cities_light.models import Country


class ProfileBase(models.Model):
    user = models.OneToOneField(User)
    country = models.ForeignKey(Country, null=True)
    dob = models.DateField(blank=True, null=True)
    GENDERS = (('M', 'Male'),
               ('F', 'Female'),
               ('O', 'Other'))
    gender = models.CharField(max_length=1, choices=GENDERS, null=True)

    class Meta:
        abstract = True


class MemberProfile(ProfileBase):
    """Profile class for ordinary users."""
    pass


class GuideProfile(ProfileBase):
    """Profile class for tour guides"""
    licensed = models.BooleanField(default=False)
    description = models.TextField()
