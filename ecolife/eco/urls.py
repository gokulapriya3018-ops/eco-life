from django.urls import path
from . import views

urlpatterns = [
    path('', views.carbon_page, name='carbon'),
    path('weekly/', views.weekly_graph, name='weekly_graph'),
    path('water/', views.water_usage, name='water'),

     
]
