from django.test import TestCase
from .models import Vulnerability

class VulnerabilityModelTest(TestCase):
    def setUp(self):
        Vulnerability.objects.create(name="Test Vulnerability", severity="High", description="Test description")

    def test_vulnerability_name(self):
        vulnerability = Vulnerability.objects.get(name="Test Vulnerability")
        self.assertEqual(vulnerability.name, "Test Vulnerability")
