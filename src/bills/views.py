from django.shortcuts import render
from .models import Bills
from django.contrib.auth import authenticate
from .forms import BillsForm
from django.views.generic import View, FormView, TemplateView
from django.utils import timezone
from django.utils import http
from django.shortcuts import redirect
from django.conf import settings
from django.core import serializers
import json
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.db.models import Sum
# Create your views here.

class BillsView(TemplateView):
	def get(self, request):
		if request.user.is_authenticated:
			context={}
			monthly_details,result= self.monthlyDetails(request)
			context['monthlyDetails']= monthly_details
			form = BillsForm
			print(context)
			context['form'] = form
			return render(request,'bills.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)
	def post(self, request):
		if request.user.is_authenticated:
			form = BillsForm(request.POST)
			context={}
			if form.is_valid():
				date = request.POST.get('date')
				date = datetime.strptime(date, '%m/%d/%Y')
				date.strftime('%Y/%m/%d')
				money = request.POST.get('money')
				billDescription = request.POST.get('billDescription')
				billType = request.POST.get('billType')
				user = request.user
				bill = Bills(user=user,date=date,
					money=money,
					billDescription=billDescription,
					billType=billType)
				bill.save()
				form = BillsForm()
				context['form']=form
				return  render(request,'bills.html',context)
			else:
				return  render(request,'bills.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)
	def monthlyDetails(self,request):
		print("Hello")
		if self.request.user.is_authenticated:
			muskaan = Bills.objects.extra(select={'month': 'strftime("%m",date)','day':'strftime("%d",date)'},order_by=['month','day'])
			month_dict={}
			for musk in muskaan:
				if str(musk.date.strftime("%B %Y")) in month_dict.keys():
					month_dict[str(musk.date.strftime("%B %Y"))].append(musk)
				else:
					month_dict[str(musk.date.strftime("%B %Y"))]=[musk]
			muskaan = Bills.objects.extra(select={'month': 'strftime("%m %Y",date)','day':'strftime("%d",date)'},order_by=['month','day'])
			result = muskaan.values('billType','month').order_by('month','billType').annotate(total_bill=Sum('money'))
			print(result)
			return month_dict,result
		else:
			redirect (settings.LOGIN_REDIRECT_URL)

def billJson(request,bill):
	if request.user.is_authenticated:
		billObj = Bills.objects.filter(id=bill)
		jsonitems = serializers.serialize("json",billObj)
		jsonitems = json.loads(jsonitems)
		return JsonResponse(jsonitems,safe=False)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)
def deleteBill(request,bill):
	if request.user.is_authenticated:
		deleted=Bills.objects.filter(id=bill).delete()
		return HttpResponse('')
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)
def editBill(request,bill):
	if request.user.is_authenticated:
		billObj =Bills.objects.filter(id=bill)
		jsonitems = serializers.serialize("json",billObj)
		jsonitems = json.loads(jsonitems)
		return JsonResponse(jsonitems,safe=False)
	else:
		return redirect(settings.LOGIN_REDIRECT_URL)





