from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail, EmailMessage
from django.dispatch import receiver
from django.core.cache import cache
from django.conf import settings

from apps.news.models import News
from .models import BecomeAPartner
from apps.brand.models import Brand
from apps.flavor.models import Flavor
from apps.vacancy.models import Vacancy
from apps.language.models import Language
from apps.partners.models import OurPartners
from apps.advantages.models import Advantages
from apps.product.models import Product, Category
from apps.content.models import Video, LogoCompany
from apps.communication.models import Contacts, Links
from apps.brand_info.models import BrandInfo, BrandHistory
from apps.production.models import Production, ProductionShort, ProductionProcess, ProductionPath


@receiver(post_save, sender=OurPartners)
@receiver(post_delete, sender=OurPartners)
def clear_our_partners_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Language)
@receiver(post_delete, sender=Language)
def clear_language_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Video)
@receiver(post_delete, sender=Video)
def clear_video_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=LogoCompany)
@receiver(post_delete, sender=LogoCompany)
def clear_logo_company_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Contacts)
@receiver(post_delete, sender=Contacts)
def clear_contacts_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Links)
@receiver(post_delete, sender=Links)
def clear_links_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Vacancy)
@receiver(post_delete, sender=Vacancy)
def clear_vacancy_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=ProductionProcess)
@receiver(post_delete, sender=ProductionProcess)
def clear_production_process_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=ProductionPath)
@receiver(post_delete, sender=ProductionPath)
def clear_production_path_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=ProductionShort)
@receiver(post_delete, sender=ProductionShort)
def clear_production_short_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Production)
@receiver(post_delete, sender=Production)
def clear_production_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Category)
@receiver(post_delete, sender=Category)
def clear_category_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def clear_product_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=BrandHistory)
@receiver(post_delete, sender=BrandHistory)
def clear_brand_history_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=BrandInfo)
@receiver(post_delete, sender=BrandInfo)
def clear_brand_info_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Advantages)
@receiver(post_delete, sender=Advantages)
def clear_advantages_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=News)
@receiver(post_delete, sender=News)
def clear_news_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Brand)
@receiver(post_delete, sender=Brand)
def clear_brand_cache(sender, **kwargs):
    cache.clear()


@receiver(post_save, sender=Flavor)
@receiver(post_delete, sender=Flavor)
def clear_flavor_cache(sender, **kwargs):
    cache.clear()


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
