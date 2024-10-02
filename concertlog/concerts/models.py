from django.db import models

class Venue(models.Model):
    venue_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    #TODO: add tags, like large, small, ticket vendor?
    
    def __str__(self):
        return self.venue_name

class Band(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)

class Concert(models.Model):
    band = models.ForeignKey(Band, on_delete=models.RESTRICT)
    supporting_acts = models.ManyToManyField(Band, blank=True, related_name="opened_for")
    date = models.DateField("concert date")
    venue = models.ForeignKey(Venue, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.band.name} on {self.date} at {self.venue.venue_name}"
