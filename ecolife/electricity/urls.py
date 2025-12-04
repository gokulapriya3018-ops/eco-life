from django.urls import path
from . import views

urlpatterns = [
    path("tracker/", views.electricity_tracker, name="electricity_tracker"),
    path("monthly-graph/", views.monthly_graph, name="monthly_graph"),
]
