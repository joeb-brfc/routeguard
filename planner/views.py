from django.shortcuts import render, redirect
from .models import Assignment, Driver, Route, Availability
from .forms import AvailabilityForm, DriverForm, RouteForm


def home(request):
    return render(request, "planner/home.html")


def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(
        request,
        "planner/assignment_list.html",
        {"assignments": assignments},
    )

def driver_list(request):
    drivers = Driver.objects.all()
    return render(
        request,
        "planner/driver_list.html",
        {"drivers": drivers},
    )

def route_list(request):
    routes = Route.objects.all()
    return render(
        request,
        "planner/route_list.html",
        {"routes": routes},
    )

def availability_list(request):
    availabilities = Availability.objects.all()
    return render(
        request,
        "planner/availability_list.html",
        {"availabilities": availabilities},
    )

def create_driver(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("driver_list")
    else:
        form = DriverForm()

    return render(
        request,
        "planner/create_driver.html",
        {"form": form},
    )

def create_route(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("route_list")
    else:
        form = RouteForm()

    return render(
        request,
        "planner/create_route.html",
        {"form": form},
    )

def create_availability(request):
    if request.method == "POST":
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("availability_list")
    else:
        form = AvailabilityForm()

    return render(
        request,
        "planner/create_availability.html",
        {"form": form},
    )