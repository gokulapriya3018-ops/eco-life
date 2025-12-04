from django.urls import path
from . import views

urlpatterns = [
    path("", views.activity_history, name="activity_history"),
]
