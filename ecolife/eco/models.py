from django.db import models
from django.contrib.auth.models import User

class CarbonHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    vehicle = models.FloatField(default=0)     # km/day
    water = models.FloatField(default=0)       # liters/day
    electricity = models.FloatField(default=0) # kWh/day
    total = models.FloatField(default=0)       # kg CO2
    eco_score = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.total} kgCO2"


