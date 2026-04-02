from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment, Driver, Route, Availability
from .forms import AssignmentForm, AvailabilityForm, DriverForm, RouteForm


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

def create_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("assignment_list")
    else:
        form = AssignmentForm()

    return render(
        request,
        "planner/create_assignment.html",
        {"form": form},
    )

def edit_driver(request, driver_id):
    #Get the specific driver by id or return 404 if not found
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == "POST":
        #Reuse the existing DriverForm, but fill it with this driver's data
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect("driver_list")
    else:
        #On first load, show form filled with the driver's current data
        form = DriverForm(instance=driver)
    return render(
        request,
        "planner/edit_driver.html",
        {"form": form, "driver": driver},
    )

def delete_driver(request, driver_id):
    # Find the driver by id, or return a 404 page if it does not exist
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == "POST":
        # If the user confirms deletion, delete the driver
        driver.delete()
        return redirect("driver_list")
    # If the page is opened normally, show the confirmation template
    return render(
        request,
        "planner/delete_driver.html",
        {"driver": driver},
    )   