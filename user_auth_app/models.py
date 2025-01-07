from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=30)
    contactColor = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def create_or_update_users(users_data):
        """
        Create or update User and UserProfile records from a list of user data.
        """
        for user_data in users_data:
            # Create or get the User instance
            user, created = User.objects.get_or_create(
                id=user_data["id"],
                defaults={
                    "username": user_data["email"],  # Use email as username
                    "email": user_data["email"],
                },
            )

            # Set the password (hashed for security)
            if created:
                user.set_password(user_data["password"])
                user.save()

            # Create or update the UserProfile instance
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    "name": user_data["name"],
                    "phone": user_data["phone"],
                    "contactColor": user_data["contactColor"],
                },
            )
