from .models import Passwords
from django.forms import ModelForm
from django.db import models
from django import forms


class PasswordForm(ModelForm):
	class Meta:
		model = Passwords
		fields = ['websiteAppName','loginId','password']
		labels = {
			'websiteAppName':'Name of Website/App',
			'loginId':'Login ID',
			'password':'Password'
		}
		widgets = {
            'password': forms.PasswordInput(),
        }
