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

# Create your views here.
class IssueView(TemplateView):
	def get(self, request):
		if request.user.is_authenticated:
			context={}
			form = IssuesForm()
			context['form']=form
			return  render(request,'issues.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)