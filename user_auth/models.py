from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have an email')

        if not password:
            raise ValueError('User must have an password')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('User must have an email')

        if not password:
            raise ValueError('User must have an password')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=256, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    
    # django.contrib.auth required fields
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    # Data memembers for permissions within the whole project
    perms = (
        ('client', 'Client'),
        ('developer', 'Developer'),
        ('project_manager', 'Project Manager'),
    )
    perm = models.CharField(max_length=32, choices=perms, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def full_name(self):
        return self.first_name + " " + self.last_name
