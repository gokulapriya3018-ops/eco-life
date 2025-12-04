from django import forms
from .models import ElectricityUsage

class ElectricityForm(forms.ModelForm):
    class Meta:
        model = ElectricityUsage
        fields = ['month','units','fan_units','ac_units','fridge_units','others_units']
