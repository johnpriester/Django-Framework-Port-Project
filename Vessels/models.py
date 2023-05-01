from django.db import models

# Create your models here.


class Vessel(models.Model):
    vessel_name = models.CharField(max_length=200)

    def __str__(self):
        return self.vessel_name


class VesselSchedule(models.Model):
    vessel = models.ForeignKey(Vessel, on_delete=models.RESTRICT)
    voyage_number = models.CharField(max_length=50)

    def __str__(self):
        return self.vessel.vessel_name + "- " + self.voyage_number


class PortCall(models.Model):
    vessel_schedule = models.ForeignKey(VesselSchedule, on_delete=models.RESTRICT)
    port = models.CharField(max_length=200)
    port_country = models.CharField(max_length=2)
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
