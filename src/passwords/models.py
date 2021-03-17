from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Passwords(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	website_app = models.CharField(max_length= 255,blank=False)
	login_id = models.CharField(max_length=255,blank=True)
	password = models.CharField(max_length= 255,blank=False)
	
