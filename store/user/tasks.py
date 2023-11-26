from celery import shared_task

from .utils import send_mail_to


@shared_task
def send_welcome_email(user_email):
    subject = 'Welcome!'
    message = 'Спасибо за регистрацию'
    recipient_list = user_email

    send_mail_to(subject, message, recipient_list)
