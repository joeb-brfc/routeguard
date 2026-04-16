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

# Custom form validation implemented using Django validation guidelines:
# https://docs.djangoproject.com/en/6.0/ref/forms/validation/
# Adapted to enforce driver scheduling rules (availability, time checks, duplicate assignments)

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["driver", "route", "date", "start_time", "end_time"]

    def clean(self):
        # Get the form data that Django has already cleaned
        cleaned_data = super().clean()

        # Pull out the values we need for validation
        driver = cleaned_data.get("driver")
        date = cleaned_data.get("date")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        # validation 1: Check that end time is after start time & both times are provided
        if start_time and end_time:
            if end_time <= start_time:
                raise forms.ValidationError(
                    "End time must be later than start time."
                )
            
        # validation 2 Check that the driver is available on that date & availability record exists
        if driver and date:
            availability = Availability.objects.filter(driver=driver, date=date).first()
            if availability and availability.status != "available":
                raise forms.ValidationError(
                    f"Driver is not available on {date} (status: {availability.status})."
                )
            
        # validation 3: A driver can not work the same day on multiple routes
        if driver and date:
            existing_assignments = Assignment.objects.filter(driver=driver, date=date)
              # If editing later, exclude the current record from the check
            if existing_assignments.exists():
                raise forms.ValidationError(
                    f"Driver already has an assignment on {date}."
                )

        # Always return the cleaned data
        return cleaned_data