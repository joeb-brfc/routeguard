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
    path("assignments/create/", views.create_assignment, name="create_assignment"),
    path("drivers/<int:driver_id>/edit/", views.edit_driver, name="edit_driver"),
    path("drivers/<int:driver_id>/delete/", views.delete_driver, name="delete_driver"),
    path("routes/<int:route_id>/edit/", views.edit_route, name="edit_route"),
    path("routes/<int:route_id>/delete/", views.delete_route, name="delete_route"),
]