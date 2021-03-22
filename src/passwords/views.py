from django.shortcuts import render
from .models import Passwords
from django.contrib.auth import authenticate
from .forms import PasswordForm
from django.views.generic import View, FormView, TemplateView
from django.utils import timezone
from django.utils import http
from django.shortcuts import redirect
from django.conf import settings
from django.core import serializers
import json
from django.http import JsonResponse, HttpResponse
# Create your views here.

class PasswordView(TemplateView):
	def get(self, request):
		if request.user.is_authenticated:
			context = {}
			form = PasswordForm
			context['form'] = form
			response = getUserPasswords(request)
			if response is not None:
				context['userPasswords'] = response
			return  render(request,'passworddisplay.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)
	def post(self, request):
		if request.user.is_authenticated:
			form = PasswordForm(request.POST)
			context={}
			response = getUserPasswords(request)
			if response is not None:
				context['userPasswords'] = response
			if form.is_valid():
				websiteAppName = request.POST.get('websiteAppName')
				loginId = request.POST.get('loginId')
				password= request.POST.get('password')
				user= request.user
				pwd= Passwords(user=user,
					websiteAppName=websiteAppName,
					loginId=loginId,
					password=password,
					)
				pwd.save()
				form = PasswordForm()
				context['form']=form
				return render(request,'passworddisplay.html',context)
def getUserPasswords(request):
	if request.user.is_authenticated:
		response=Passwords.objects.filter(user=request.user.id)
		if response is None:
			return None
		else:
			return response
def deletePassword(request,password):
	if request.user.is_authenticated:
		deleted=Passwords.objects.filter(id=password).delete()
		return HttpResponse('')
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)
def updatePassword(request,password):
	if request.user.is_authenticated:
		passwordObj = Passwords.objects.filter(id=password)
		jsonitems = serializers.serialize("json",passwordObj)
		jsonitems = json.loads(jsonitems)
		return JsonResponse(jsonitems,safe=False)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)

