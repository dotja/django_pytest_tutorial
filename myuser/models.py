from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):
	def create_user(self, email, name, password=None):
		my_user = self.model(email=self.normalize_email(email), name=name)
		my_user.set_password(password)
		my_user.save()
		return my_user


class MyUser(AbstractBaseUser):
	email = models.EmailField(max_length=150, unique=True)
	name = models.CharField(max_length=100, blank=True)
	objects = MyUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']


