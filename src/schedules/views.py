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
from django.http import JsonResponse, HttpResponse
# Create your views here.

class ScheduleView(TemplateView):
	def get(self, request):
		if request.user.is_authenticated:
			context = {}
			form = ScheduleForm
			context['form'] = form
			return render(request,'scheduledisplay.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)
	def post(self, request):
		if request.user.is_authenticated:
			form = ScheduleForm(request.POST)
			context={}
			if form.isValid():
				eventName = request.POST.get('eventName')
				eventDateTime = request.POST.get('eventDateTime')
				eventDuration = request.POST.get('eventDuration')
				eventType = request.POST.get('eventType')
				user = request.user
				schedule = Schedules(user=user,eventName=eventName,
					eventDateTime=eventDateTime,
					eventDuration=eventDuration,
					eventType=eventType)
				schedule.save()
				form = ScheduleForm()
				context['form']=form
				return  render(request,'scheduledisplay.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)