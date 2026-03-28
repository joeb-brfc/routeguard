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

    def clean(self):
        # Get the form data that Django has already cleaned
        cleaned_data = super().clean()

        # Pull out the two time fields
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        # Check that the end time is later than the start time
        if start_time and end_time:
            if end_time <= start_time:
                raise forms.ValidationError(
                    "End time must be later than start time."
                )

        # Always return the cleaned data
        return cleaned_data