from django.db import models

class WatchlistItem(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.DateField(null=True, blank=True)
    review = models.TextField()