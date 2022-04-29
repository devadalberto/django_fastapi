from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import UserManager

class User(AbstractUser):
    pass
	#is_dtag = models.BooleanField(default=True)

class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    password2 = None

    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
