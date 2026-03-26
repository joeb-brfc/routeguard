from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("assignments/", views.assignment_list, name="assignment_list"),
    path("drivers/", views.driver_list, name="driver_list"),
    path("routes/", views.route_list, name="route_list"),
]