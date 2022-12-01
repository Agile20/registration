from django.core.mail import EmailMessage
from django.conf import settings

def message(email):
    mail = EmailMessage(
        'Алмаз лох',
        'Вас хакнули ХАХАХАХХААХАХХАХАХАХА',
        settings.EMAIL_HOST_USER,
        [email]        
    )
    mail.send()