from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ActivityHistory

@login_required
def activity_history(request):
    logs = ActivityHistory.objects.filter(user=request.user).order_by('-date')
    return render(request, "history/activity_history.html", {"logs": logs})
