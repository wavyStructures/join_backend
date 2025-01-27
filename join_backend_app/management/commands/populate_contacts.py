from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from join_backend_app.models import Contact 

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate contacts with all users in the system and ensure guest user exists'

    def handle(self, *args, **kwargs):
        guest_user, created = User.objects.get_or_create(username="guest", defaults={"password": "guestpassword"})

        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created guest user'))

        users = User.objects.all()

        for user in users:
            Contact.objects.create(
                username=user.username,
                phone=user.phone,
                email=user.email,
                contactColor='#FF5733',
                contact_is_a_user=True,
                user=guest_user.id  
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated contacts with users'))
        