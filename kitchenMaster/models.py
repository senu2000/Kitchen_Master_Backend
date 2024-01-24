from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date


# Create your models here.
class User(AbstractUser):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'username', 'password', 'role']

    def __str__(self):
        return "{}".format(self.email)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    serving_size = models.IntegerField()
    prep_time = models.IntegerField()
    instruction = models.TextField(blank=True)
    recipe_image = models.ImageField(upload_to='images')

    fk = models.ForeignKey(User, on_delete=models.CASCADE)  # foreignkey

    @property
    def firstname(self):
        return self.fk.firstname

    @property
    def lastname(self):
        return self.fk.lastname

    @property
    def username(self):
        return self.fk.username

    @property
    def email(self):
        return self.fk.email
