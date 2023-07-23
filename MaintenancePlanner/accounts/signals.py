from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver

from MaintenancePlanner.accounts.models import Profile, AppUser


@receiver(post_save, sender=AppUser)
def create_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AppUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
