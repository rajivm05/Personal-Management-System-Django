from .models import Issues
from django.forms import ModelForm
from django.db import models
from django import forms

class IssuesForm(ModelForm):
	class Meta:
		model = Issues
		fields = ['issueName','issueDescription','dueDate']
		labels = {
			'issueName':'Issue',
			'issueDescription':'Description of issue',
			'dueDate':'Due Date',
		}
		widgets = {
            'dueDate': forms.DateInput(attrs={'class':'datepicker'}),
        }
		
