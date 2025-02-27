from django.db import models

# Create your models here.

class Vulnerability(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    severity = models.CharField(max_length=50)
    description = models.TextField()
    date_reported = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
