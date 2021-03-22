from django.shortcuts import render
from .models import Issues
from django.contrib.auth import authenticate
from .forms import IssuesForm
from django.views.generic import View, FormView, TemplateView
from django.utils import timezone
from django.utils import http
from django.shortcuts import redirect
from django.conf import settings
from django.core import serializers
import json
from django.http import JsonResponse, HttpResponse
from datetime import datetime

# Create your views here.
class IssueView(TemplateView):
	def get(self, request):
		if request.user.is_authenticated:
			context={}
			current_issue = self.get_current_issue(request)
			if current_issue is not None:
				context['issues'] = current_issue
				# context=self.sortCurrentTodo(current_todo)
			form = IssuesForm()
			context['form']=form
			return  render(request,'issues.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)

	def post(self, request):
		print(self.request.user.id)
		form = IssuesForm(request.POST)
		context={}
		current_issue = self.get_current_issue(request)
		if current_issue is not None:
			context['issues'] = current_issue
		if form.is_valid():
			issueName= request.POST.get('issueName')
			issueDescription = request.POST.get('issueDescription')
			startDate = timezone.now()
			lastProgress = timezone.now()
			user= request.user
			issue= Issues(user=user,
				issueName=issueName,
				issueDescription=issueDescription,
				startDate=startDate,
				lastProgress=lastProgress,
				)
			issue.save()
			current_issue = self.get_current_issue(request)
			if current_issue is not None:
				context['issue'] = current_issue
				# context=self.sortCurrentIssue(current_issue)
			form = IssuesForm()
			context['form']=form
			return render(request,'issues.html',context)

	def get_current_issue(self,request):
		response=Issues.objects.filter(user=request.user.id)
		if response is None:
			return None
		else:
			return response

def issuesJson(request,issue):
	if request.user.is_authenticated:
		issueObj = Issues.objects.filter(id=issue)
		jsonitems = serializers.serialize("json",issueObj)
		jsonitems = json.loads(jsonitems)
		return JsonResponse(jsonitems,safe=False)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)
def deleteIssue(request,issue):
	if request.user.is_authenticated:
		deleted=Issues.objects.filter(id=issue).delete()
		return HttpResponse('')
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)
def editIssue(request,issue):
	if request.user.is_authenticated:
		issueObj =Issues.objects.filter(id=task)
		jsonitems = serializers.serialize("json",issueObj)
		jsonitems = json.loads(jsonitems)
		return JsonResponse(jsonitems,safe=False)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)