from django.db import models
from django.contrib.auth.models import User

class ActivityHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    carbon = models.FloatField(default=0)       
    water = models.FloatField(default=0)       
    electricity = models.FloatField(default=0)  

    def total_score(self):
        return self.carbon + self.water + self.electricity

    def __str__(self):
        return f"{self.user.username} - {self.date}"
