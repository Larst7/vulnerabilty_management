from django.contrib import admin
from django.urls import path, include
from . import views  # Import the views from your project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vulnerabilities/', include('vulnerabilities.urls')),  # Ensure this is correct
    path('', views.home, name='home'),  # Add this line for the root URL
]

