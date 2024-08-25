from django.urls import path
from .views import VulnerabilityListCreateView, VulnerabilityDetailView

urlpatterns = [
    path('vulnerabilities/', VulnerabilityListCreateView.as_view(), name='vulnerability-list-create'),
    path('vulnerabilities/<int:pk>/', VulnerabilityDetailView.as_view(), name='vulnerability-detail'),
]
