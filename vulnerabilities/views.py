from django.shortcuts import render
from .models import Vulnerability  # Assuming Vulnerability is your model name

def vulnerability_list(request):
    vulnerabilities = Vulnerability.objects.all()  # Fetch all vulnerabilities
    return render(request, 'vulnerabilities/vulnerability_list.html', {'vulnerabilities': vulnerabilities})
