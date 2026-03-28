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
        driver = cleaned_data.get("driver")
        date = cleaned_data.get("date")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        # validation 1: Check that end time is after start time
        if start_time and end_time:
            if end_time <= start_time:
                raise forms.ValidationError(
                    "End time must be later than start time."
                )
            
        # validation 2 Check that the driver is available on that date
        if driver and date:
            availability = Availability.objects.filter(driver=driver, date=date).first()
            if availability and availability.status != "available":
                raise forms.ValidationError(
                    f"Driver is not available on {date} (status: {availability.status})."
                )

        # Always return the cleaned data
        return cleaned_data