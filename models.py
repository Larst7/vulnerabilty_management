# vulnerability_management/models.py

from django.db import models

class Vulnerability(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=50)
    reported_date = models.DateField()
    # Add more fields as needed

    def __str__(self):
        return self.name
