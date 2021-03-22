from .models import Issues
from django.forms import ModelForm
from django.db import models
from django import forms
from django.conf import settings
from django.forms.models import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField  

class IssuesForm(ModelForm):
	class Meta:
		model = Issues
		fields = ['issueName','issueDescription']
		labels = {
			'issueName':'Issue',
			'issueDescription':'Description of issue',
		}