from django.shortcuts import render
from .models import Schedules
from django.contrib.auth import authenticate
from .forms import ScheduleForm
from django.views.generic import View, FormView, TemplateView
from django.utils import timezone
from django.utils import http
from django.shortcuts import redirect
from django.conf import settings
from django.core import serializers
import json
from django.contrib import messages
from django.http import JsonResponse, HttpResponse

# Create your views here.
class ScheduleView(TemplateView):
	def get(self, request):
		if request.user.is_authenticated:
			context = {}
			form = ScheduleForm
			context['form'] = form
			currentSchedule = getSchedule(request)
			if currentSchedule is not None:
				context['currentSchedule'] = currentSchedule
			context['sendAlert']="false"
			return render(request,'scheduledisplay.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)

	def post(self, request):
		if request.user.is_authenticated:
			form = ScheduleForm(request.POST)
			context={}
			context['sendAlert']="false"
			currentSchedule = getSchedule(request)
			if currentSchedule is not None:
				context['currentSchedule'] = currentSchedule
			eventName = request.POST.get('eventName')
			eventStart = request.POST.get('eventStart')
			eventEnd = request.POST.get('eventEnd')
			eventType = request.POST.get('eventType')
			user = request.user
			if eventEnd>eventStart:
				schedule = Schedules(user=user,eventName=eventName,
					eventStart=eventStart,
					eventEnd=eventEnd,
					eventType=eventType)
				schedule.save()
				form = ScheduleForm()
				context['form']=form
				return  render(request,'scheduledisplay.html',context)
			else:
				form = ScheduleForm()
				context['form']=form
				context['sendAlert']="true"
				return  render(request,'scheduledisplay.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)
	

def getSchedule(request):
	if request.user.is_authenticated:
		response = Schedules.objects.filter(user=request.user).order_by('eventStart')
		if response is not None:
			return response
		else:
			return None
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)

def deleteSchedule(request,schedule):
	if request.user.is_authenticated:
		deleted=Schedules.objects.filter(id=schedule).delete()
		return HttpResponse('')
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)

def editSchedule(request,schedule):
	if request.user.is_authenticated:
		scheduleObj = Schedules.objects.filter(id=schedule)
		jsonitems = serializers.serialize("json",scheduleObj)
		jsonitems = json.loads(jsonitems)
		return JsonResponse(jsonitems,safe=False)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)