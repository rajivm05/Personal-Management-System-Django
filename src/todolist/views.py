from django.shortcuts import render
from .models import ToDoList
from django.contrib.auth import authenticate
from .forms import ToDoListForm
from django.views.generic import View, FormView, TemplateView
from django.utils import timezone
from django.utils import http
from django.shortcuts import redirect
from django.conf import settings
from django.core import serializers
import json
from django.http import JsonResponse, HttpResponse

# Create your views here.
class CreateToDoListView(TemplateView):
	def get(self, request):
		if request.user.is_authenticated:
			context={}
			current_todo = self.get_current_todolist(request)
			if current_todo is not None:
				# context['todolist'] = current_todo
				context=self.sortCurrentTodo(current_todo)
			form = ToDoListForm()
			context['form']=form
			return  render(request,'todolistdisplay.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)

	def post(self, request):
		print(self.request.user.id)
		form = ToDoListForm(request.POST)
		context={}
		if form.is_valid():
			taskName= request.POST.get('taskName')
			taskType= request.POST.get('taskType')
			taskDescription = request.POST.get('taskDescription')
			date_added = timezone.now()
			user= request.user
			task= ToDoList(user=user,
				taskName=taskName,
				taskDescription=taskDescription,
				date_added=date_added,
				taskType=taskType)
			task.save()
			current_todo = self.get_current_todolist(request)
			if current_todo is not None:
				# context['todolist'] = current_todo
				context=self.sortCurrentTodo(current_todo)
			form = ToDoListForm()
			context['form']=form
			return render(request,'todolistdisplay.html',context)
	def get_current_todolist(self,request):
		response=ToDoList.objects.filter(user=request.user.id)
		if response is None:
			return None
		else:
			return response
	def sortCurrentTodo(self,current_todo):
		sortedCurrentTodo={'Academic':list([]),'Administrative': list([]),'Personal':list([]),'Research':list([])}
		print(sortedCurrentTodo)
		for task in current_todo:
			sortedCurrentTodo[task.taskType].append(task)
		return sortedCurrentTodo
def taskJson(request,task):
	if request.user.is_authenticated:
		taskObj = ToDoList.objects.filter(id=task)
		jsonitems = serializers.serialize("json",taskObj)
		jsonitems = json.loads(jsonitems)
		return JsonResponse(jsonitems,safe=False)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)
def deleteJson(request,task):
	if request.user.is_authenticated:
		deleted=ToDoList.objects.filter(id=task).delete()
		return HttpResponse('')
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)



