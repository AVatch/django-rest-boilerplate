from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves an Account with the given
        minimal requirements
        """
        if not email:
            raise ValueError('Account must have an email address')

        account = self.model(
                email=self.normalize_email(email),
        )

        account.set_password(password)

        account.save(using=self._db)
        return account

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser account
        """
        account = self.create_user(email, password)
        
        account.is_admin = True
        account.is_staff = True
        account.is_superuser = True

        account.save(using=self._db)
        return account


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return '% %' % (self.first_name, self.last_name)

    def get_short_name(self):
        return '%s' % (self.email)

    def has_perm(self, perm, obj=None):
        """Does the user ahve a specific permission?"""
        # Simplest answer is yes
        return True

    def has_module_perms(self, app_level):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest answer is yes
        return True

    class Meta:
        ordering = ('-time_created', )

    def __str__(self):
        return self.get_full_name()



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Generate a token every time a new account object
    is created.
    """
    if created:
        Token.objects.create(user=instance)

