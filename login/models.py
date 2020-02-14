from django.db import models
from django.contrib.auth import models as model
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email_address = models.EmailField()
	username = models.CharField(unique=True)
	profile_picture = models.ImageField()
	# sex_choices = ((MALE, 'Male'), (FEMALE, 'Female'),)
	# sex = models.CharField(choices = sex_choices, default=MALE)
	bio = models.TextField()

	def __str__(self):
	 return self.first_name, self.last_name