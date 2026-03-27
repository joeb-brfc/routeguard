from django import forms
from .models import Assignment, Availability, Driver, Route


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["name", "employee_id", "active"]

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ["name", "destination", "estimated_hours"]

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ["driver", "date", "status"]

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["driver", "route", "date", "start_time", "end_time"]