from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class UserManager(BaseUserManager):
    groups = models.ManyToManyField(Group, blank=True)

    def _create_user(self, email, password=None, user_type=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, user_type=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, user_type, **extra_fields)

    def create_superuser(self, email, password=None, user_type=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, user_type, **extra_fields)

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('A', 'Admin'),
        ('C', 'Customer'),
    )

    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='C')

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'user_type']


    objects = UserManager()


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)






class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    def __str__(self):
        return self.name 


class CustomPermissions(models.Model):
    class Meta:
        permissions = [
            ("admin_permissions", "Can manage users, system configurations, and overall system settings"),
            ("customer_permissions", " receive reminders, and access payment history"),
        ]


class SwiftConnection(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    id = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=255)
    companyAddress= models.CharField(max_length=255)
    contactPhone = models.CharField(max_length=255)
    contactEmail = models.CharField(max_length=255)
    status= models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.companyName


