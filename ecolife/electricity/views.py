from django.shortcuts import render, redirect
from .forms import ElectricityForm
from .models import ElectricityUsage
from django.contrib.auth.decorators import login_required

@login_required
def electricity_tracker(request):
    if request.method == "POST":
        form = ElectricityForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user

            # emission calculation — 0.82 kg per unit in India
            data.carbon_emission = data.units * 0.82  
            data.save()
            return redirect("monthly_graph")
    else:
        form = ElectricityForm()

    return render(request, "electricity/electricity_tracker.html", {"form": form})


@login_required
def monthly_graph(request):
    usage = ElectricityUsage.objects.filter(user=request.user)

    months = [i.month for i in usage]
    emissions = [i.carbon_emission for i in usage]

    # pie chart
    if usage:
        last = usage.last()
        pie_data = [
            last.fan_units,
            last.ac_units,
            last.fridge_units,
            last.others_units
        ]
    else:
        pie_data = [0,0,0,0]

    return render(request, "electricity/monthly_graph.html", {
        "months": months,
        "emissions": emissions,
        "pie_data": pie_data
    })
