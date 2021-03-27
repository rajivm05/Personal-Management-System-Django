from django.db import models
from django.contrib.auth.models import User
from django.db.models import Func
# Create your models here.
class Bills(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=False)
	money = models.FloatField()
	billDescription = models.CharField(max_length=10000)
	billTypes_list = (('Monthly Payments','Monthly Payments'),('Personal', 'Personal'),('Domestic','Domestic'),('Travels','Travels'),('Food','Food'),('Entertainment','Entertainment'))
	billType = models.CharField(max_length=255,choices=billTypes_list,default='Monthly Payments')
		
	def __str__(self):
		return self.billDescription
