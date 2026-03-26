from django.shortcuts import render
from .models import Assignment


def home(request):
    return render(request, "planner/home.html")


def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(
        request,
        "planner/assignment_list.html",
        {"assignments": assignments},
    )