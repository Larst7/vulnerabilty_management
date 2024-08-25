from rest_framework import generics
from .models import Vulnerability
from .serializers import VulnerabilitySerializer

class VulnerabilityListCreateView(generics.ListCreateAPIView):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer

class VulnerabilityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer
