from .models import Schedules
from django.forms import ModelForm
from django.db import models
from django import forms

class ScheduleForm(ModelForm):
	class Meta:
		model = Schedules
		fields = ['eventName','eventDate','eventTime','eventDuration','eventType']
		labels = {
			'eventName':'Name of event',
			'eventDate':'Date of event',
			'eventTime':'Time of event',
			'eventDuration':'Duration of Event',
			'eventType':'Type of event'
		}
		# widgets={
		# 	'eventDateTime':forms.DateTimeInput(),
		# 	'eventDuration':forms.TimeInput(),
		# }