from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def vulnerability_list(request):
    return render(request, 'vulnerabilities/vulnerability_list.html')
