from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Issues(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	issueName = models.CharField(max_length=10000)
	issueDescription = models.CharField(max_length=10000,blank=True)
	startDate = models.DateField(auto_now_add=True)
	lastProgress = models.DateField(auto_now=True)
	dueDate = models.DateField(blank=True)
	mark_as_complete = models.BooleanField(default=False)

	def __str__(self):
		return self.issueName