from django.test import TestCase
from .models import Vulnerability

class VulnerabilityModelTest(TestCase):

    def test_vulnerability_creation(self):
        vulnerability = Vulnerability.objects.create(
            title="Test Vulnerability",
            description="This is a test vulnerability.",
            severity="High",
        )
        self.assertEqual(str(vulnerability), "Test Vulnerability")
