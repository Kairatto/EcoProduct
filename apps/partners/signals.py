from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import BecomeAPartner


@receiver(post_save, sender=BecomeAPartner)
def send_partner_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Новая заявка на партнерство, на сайте Eco-Product'
        message = f'''
        Имя: {instance.name}
        Страна: {instance.country}
        Email: {instance.email}
        Описание: {instance.description}
        '''
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_EMAIL],
            reply_to=[instance.email],
        )
        email.send(fail_silently=False)
