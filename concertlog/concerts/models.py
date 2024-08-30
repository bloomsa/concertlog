from django.db import models

# Create your models here.

class Venue(models.Model):
    venue_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()

class Concert(models.Model):
    band_name = models.CharField(max_length=200)
    date = models.DateTimeField("concert date")
    venue = models.ForeignKey(Venue, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.band_name} on {self.date} at {self.venue.venue_name}"
    