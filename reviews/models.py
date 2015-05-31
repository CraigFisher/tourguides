from django.db import models
from django.contrib.auth.models import User
from profiles.models import GuideProfile
from tours.models import Tour


class Review(models.Model):
    creator = models.ForeignKey(User)
    creation_time = models.DateTimeField()
    description = models.TextField()
    RATINGS = ((0.5, 0.5),
               (1, 1),
               (1.5, 1.5),
               (2, 2),
               (2.5, 2.5),
               (3, 3),
               (3.5, 3.5),
               (4, 4),
               (4.5, 4.5),
               (5, 5))
    rating = models.DecimalField(max_digits=2, decimal_places=1, choices=RATINGS)

    class Meta:
        abstract = True


class TourReview(Review):
    tour = models.ForeignKey(Tour)


class GuideReview(Review):
    guide = models.ForeignKey(GuideProfile)


class ReviewDeletionRequest(models.Model):
    requester = models.ForeignKey(GuideProfile)
    creation_time = models.DateTimeField()
    reason = models.CharField(max_length=400)

    class Meta:
        abstract = True


class TourReviewDeletionRequest(ReviewDeletionRequest):
    review = models.ForeignKey(TourReview)


class GuideReviewDeletionRequest(ReviewDeletionRequest):
    review = models.ForeignKey(GuideReview)
