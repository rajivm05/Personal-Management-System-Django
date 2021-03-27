from .models import Bills
from django.forms import ModelForm
from django.db import models
from django import forms
from django.conf import settings
from django.forms.models import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField  


class BillsForm(ModelForm):
	class Meta:
		model = Bills
		fields = ['date','money','billDescription','billType']
		labels = {
			'date':'Date',
			'money': 'Money',
			'billDescription':'Description',
			'billType':'Type'
		}
		widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker',}),
        }