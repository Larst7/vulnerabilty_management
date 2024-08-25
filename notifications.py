from django.core.mail import send_mail

def send_vulnerability_alert(user_email, vulnerability):
    subject = f'Critical Vulnerability Detected: {vulnerability.title}'
    message = f"""
    A critical vulnerability has been detected:
    
    Title: {vulnerability.title}
    Severity: {vulnerability.severity}
    Description: {vulnerability.description}
    
    Please take immediate action to resolve this issue.
    """
    send_mail(
        subject,
        message,
        'noreply@vulnmanagement.com',
        [user_email],
    )
