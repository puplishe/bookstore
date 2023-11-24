from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    subject = 'Welcome!'
    message = 'Спасибо за регистрацию'
    from_email = 'email@example.com'
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)