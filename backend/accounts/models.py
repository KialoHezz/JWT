from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User Must Have an Email Addresses')
        # User Inputs HEZZYKIALO@GMAIL THEN email will be normalized into hezzykialo@gmail.com
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)

        user.save()

        return user

        

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Specified that all objects for the class come from the UserAccountManager
    objects = UserAccountManager()

    # Set the USERNAME_FIELD -- which defines the unique identifier  for the model when login
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email