from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("assignments/", views.assignment_list, name="assignment_list"),
    path("drivers/", views.driver_list, name="driver_list"),
    path("routes/", views.route_list, name="route_list"),
    path("availabilities/", views.availability_list, name="availability_list"),
    path("drivers/create/", views.create_driver, name="create_driver"),
    path("routes/create/", views.create_route, name="create_route"),
    path("availabilities/create/", views.create_availability, name="create_availability"),
]