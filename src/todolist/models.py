from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ToDoList(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	taskName = models.CharField(max_length=10000)
	taskDescription = models.CharField(max_length=10000)
	date_added = models.DateTimeField(auto_now_add=True)
	taskTypes_list = (('Academic','Academic'),('Administrative', 'Administrative'),('Personal','Personal'),('Research','Research'))
	taskType = models.CharField(max_length=255,choices=taskTypes_list,default='Academic')
	mark_as_complete = models.BooleanField(default=False)
	
	def __str__(self):
		return self.taskName
