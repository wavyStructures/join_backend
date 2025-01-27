from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def add_user_to_contacts(sender, instance, created, **kwargs):
    """
    This function automatically adds a new user as a contact for all existing users
    when a new user registers.
    """
    if created:
        # For each user in the system (excluding the newly created user), add them as a contact
        for user in User.objects.exclude(id=instance.id):
            Contact.objects.get_or_create(user=user, email=instance.email) 