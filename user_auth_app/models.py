from django.contrib.auth.models import User
from django.db import models
from join_backend_app.models import Contact




class UserProfile(models.Model):

    default_contact = Contact.objects.first()  # You can use any condition here to get a valid Contact instance

    # Use a string reference to avoid circular import
    contact = models.OneToOneField('join_backend_app.Contact', on_delete=models.CASCADE, default=some_default_contact)    
    name = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=30)
    contactColor = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Token(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate_token(self):
        """Generates a secure random token."""
        return secrets.token_urlsafe(64)

    @classmethod
    def create_token_for_user(cls, user):
        token = cls(user=user, token=secrets.token_urlsafe(64))
        token.save()
        return token

    def __str__(self):
        return self.token






    # @staticmethod
    # def create_or_update_users(users_data):
    #     """
    #     Create or update User and UserProfile records from a list of user data.
    #     """
    #     for user_data in users_data:
    #         # Create or get the User instance
    #         user, created = User.objects.get_or_create(
    #             id=user_data["id"],
    #             defaults={
    #                 "username": user_data["email"],  # Use email as username
    #                 "email": user_data["email"],
    #             },
    #         )

    #         # Set the password (hashed for security)
    #         if created:
    #             user.set_password(user_data["password"])
    #             user.save()

    #         # Create or update the UserProfile instance
    #         UserProfile.objects.update_or_create(
    #             user=user,
    #             defaults={
    #                 "name": user_data["name"],
    #                 "phone": user_data["phone"],
    #                 "contactColor": user_data["contactColor"],
    #             },
    #         )
