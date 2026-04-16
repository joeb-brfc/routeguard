from django.db import models

# Model structure inspired by Django documentation:
# https://docs.djangoproject.com/en/6.0/topics/db/models/

class Driver(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    estimated_hours = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.name


class Availability(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("rest", "Rest"),
        ("holiday", "Holiday"),
        ("sick", "Sick"),
        ("unavailable", "Unavailable"),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.driver} - {self.date} - {self.status}"


class Assignment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.driver} - {self.route} - {self.date}"