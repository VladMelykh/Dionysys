import datetime
from django.db import models
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

class our_user(models.Model):
    """User (name, email, password, his requests, his propositions)"""
    email = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=80, default=None, null=True)
    his_requests = models.CharField(max_length=1000, default=None, null=True)
    his_propositions = models.CharField(max_length=1000, default=None, null=True)
    

    def __str__(self):
        return self.email

class Request(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    request_text = models.CharField(max_length=300)
    cat = models.CharField(max_length=40)


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.title


class Proposition(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    proposition_text = models.CharField(max_length=300)
    cat = models.CharField(max_length=40)
    field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.title

class Category(models.Model):
    cat_text = models.CharField(max_length=40)

    def __str__(self):
        return self.cat_text