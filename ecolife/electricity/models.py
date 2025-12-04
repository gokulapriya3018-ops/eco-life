from django.db import models
from django.contrib.auth.models import User

class ElectricityUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    units = models.FloatField()  
    fan_units = models.FloatField(default=0)
    ac_units = models.FloatField(default=0)
    fridge_units = models.FloatField(default=0)
    others_units = models.FloatField(default=0)
    carbon_emission = models.FloatField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.month}"
