from django.test import TestCase
from .models import Vulnerability
from .scanner import run_nmap_scan

class VulnerabilityModelTest(TestCase):
    def test_create_vulnerability(self):
        vulnerability = Vulnerability.objects.create(
            title="SQL Injection",
            description="SQL injection vulnerability in login form",
            severity="High"
        )
        self.assertEqual(vulnerability.title, "SQL Injection")
        self.assertEqual(vulnerability.severity, "High")

class ScannerTest(TestCase):
    def test_nmap_scan(self):
        results = run_nmap_scan('127.0.0.1')
        self.assertTrue(len(results) > 0)
