from django.shortcuts import render
from stations.models import Station

# List view
from django.views.generic import ListView
class StationList(ListView):
    model = Station
    context_object_name = 'stations'
    
# Create view
from django.views.generic import CreateView
