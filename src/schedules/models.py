from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Schedules(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	eventName = models.CharField(max_length=255, blank=False)
	eventStart = models.DateTimeField(blank=False)
	eventEnd = models.DateTimeField(blank=False,help_text="The end time must be later than the start time.")
	eventTypes_list = (('Academic','Academic'),('Administrative', 'Administrative'),('Personal','Personal'),('Research','Research'))
	eventType = models.CharField(max_length=255,choices=eventTypes_list,default='Academic')

	def __str__(self):
		return self.eventName