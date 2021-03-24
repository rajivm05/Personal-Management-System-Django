from .models import Schedules
from django.forms import ModelForm
from django.db import models
from django.contrib import admin
from django import forms

class DateInput(forms.DateInput):
	input_type = 'datetime-local'

class ScheduleForm(ModelForm):
	class Meta:
		model = Schedules
		fields = ['eventName','eventStart','eventEnd','eventType']
		labels = {	
			'eventName':'Name of event',
			'eventStart':'Start',
			'eventEnd':'End',
			'eventType':'Type of event'
		}
		widgets = {
		'eventStart':DateInput(),
		'eventEnd':DateInput()
		}
		def clean_end(self):
			if self.cleaned_data['end'] <= self.cleaned_data['start']:
				raise forms.ValidationError("The end time must be later than start time.")
			return self.cleaned_data['end']

	
		