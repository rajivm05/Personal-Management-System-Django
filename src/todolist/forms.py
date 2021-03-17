from .models import ToDoList
from django.forms import ModelForm
from django.db import models


class ToDoListForm(ModelForm):
	class Meta:
		model = ToDoList
		fields = ['taskName','taskDescription','taskType']
		labels = {
			'taskName':'Task Name',
			'taskDescription':'Task Description',
			'taskType':'Task Type'
		}
		
