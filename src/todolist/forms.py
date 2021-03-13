from .models import ToDoList
from django.forms import ModelForm

class ToDoListForm(ModelForm):
	class Meta:
		model = ToDoList
		fields = ['taskName','taskDescription','taskType']
		
