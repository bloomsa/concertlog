from django.urls import path

from . import views

app_name = "concertlog"
urlpatterns = [
    path("", views.index, name="index"),
    path('venues', views.venue_list, name="venue list")
]
