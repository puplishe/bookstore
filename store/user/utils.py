from django.core.mail import send_mail
from store.settings import EMAIL_HOST_USER

def send_mail_to(subject, message, reciever):
    send_mail(subject, message, EMAIL_HOST_USER, [reciever], fail_silently=False)