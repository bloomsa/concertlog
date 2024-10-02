from django.http import HttpResponse
from django.shortcuts import render

from .models import Venue
# Create your views here.

def index(request):
    return HttpResponse("Welcome to sam's concert-log~!")

def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'concerts/venue_index.html', {'venues': venues}) 