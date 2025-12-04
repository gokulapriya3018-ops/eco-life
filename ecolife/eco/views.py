from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import CarbonHistory

@login_required
def carbon_page(request):
    result = None
    eco_score = None

    if request.method == "POST":
        try:
            km = float(request.POST.get("km", 0))
            water = float(request.POST.get("water", 0))
            electricity = float(request.POST.get("electricity", 0))
        except ValueError:
            km = water = electricity = 0.0

        vehicle_emission = km * 0.21
        water_emission = water * 0.0003
        electricity_emission = electricity * 0.85

        total = vehicle_emission + water_emission + electricity_emission
        result = round(total, 2)

        if total < 5:
            eco_score = 100
        elif total < 10:
            eco_score = 80
        elif total < 20:
            eco_score = 60
        else:
            eco_score = 40

        CarbonHistory.objects.update_or_create(
            user=request.user,
            date=date.today(),
            defaults={
                'vehicle': km,
                'water': water,
                'electricity': electricity,
                'total': total,
                'eco_score': eco_score,
            }
        )

    # fetch today record (if any) to pre-fill
    today_record = CarbonHistory.objects.filter(user=request.user, date=date.today()).first()
    context = {
        'result': result or (today_record.total if today_record else None),
        'eco_score': eco_score or (today_record.eco_score if today_record else None),
        'today_record': today_record,
    }
    return render(request, 'eco/carbon.html', context)


@login_required
def weekly_graph(request):
    today = date.today()
    week_dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
    labels = []
    totals = []
    for d in week_dates:
        labels.append(d.strftime("%d %b"))
        rec = CarbonHistory.objects.filter(user=request.user, date=d).first()
        totals.append(round(rec.total, 2) if rec else 0)
    return render(request, 'eco/weekly_graph.html', {'labels': labels, 'totals': totals})

from django.contrib.auth.decorators import login_required

@login_required
def water_usage(request):
    result = None

    if request.method == "POST":
        water = float(request.POST.get("water"))
        result = round(water * 0.001, 3)   # Example CO₂ formula

    return render(request, "eco/water.html", {"result": result})



