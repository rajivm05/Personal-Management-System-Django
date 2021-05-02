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
			monthly_details,result,result_monthTotal= self.monthlyDetails(request)
			context['monthlyDetails']= monthly_details
			result= preprocessMonth(result)
			result_monthTotal= preprocessMonth(result_monthTotal)
			print("Final ",result)
			context['result']=result
			context['result_monthTotal']= result_monthTotal
			form = BillsForm
			print("\n\n\n---------",result_monthTotal,"-----------\n\n\n")
			print(context)
			context['form'] = form
			cat_bill = getCategoricalBills(request)
			context['cat_bill']= cat_bill
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
				monthly_details,result,result_monthTotal= self.monthlyDetails(request)
				context['monthlyDetails']= monthly_details
				result= preprocessMonth(result)
				result_monthTotal = preprocessMonth(result_monthTotal)
				context['result']=result
				context['result_monthTotal']= result_monthTotal
				print("\n\n\n",result_monthTotal,"\n\n\n")
				form = BillsForm()
				context['form']=form
				cat_bill = getCategoricalBills(request)
				
				context['cat_bill']= cat_bill
				return  render(request,'bills.html',context)
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)
	def monthlyDetails(self,request):
		print("Hello")
		if self.request.user.is_authenticated:
			muskaan = Bills.objects.extra(select={'month': 'strftime("%m",date)','day':'strftime("%d",date)', 'year':'strftime("%Y",date)'},order_by=['year','month','day'])
			print("\n\n",muskaan,"\n\n")
			month_dict={}
			for musk in muskaan:
				if str(musk.date.strftime("%B %Y")) in month_dict.keys():
					month_dict[str(musk.date.strftime("%B %Y"))].append(musk)
				else:
					month_dict[str(musk.date.strftime("%B %Y"))]=[musk]
			muskaan = Bills.objects.extra(select={'month': 'strftime("%m %Y",date)','day':'strftime("%d",date)'},order_by=['month','day'])
			result = muskaan.values('billType','month').order_by('month','billType').annotate(total_bill=Sum('money'))
			result_monthTotal = muskaan.values('month').order_by('month').annotate(monthlyBill=Sum('money'))
			return month_dict,result,result_monthTotal
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
def preprocessMonth(resultSet):
	month_int = {1:"January",2:"February",3:"March",4:"April",
				5:"May",6:"June",7:"July",8:"August",9:"September",
				10:"October",11:"November",12:"December"}
	for d in resultSet:
		d['month']= month_int[int(d['month'][0:2])]+d['month'][2:]
	return resultSet

def getCategoricalBills(request):
	if request.user.is_authenticated:
		categories = ['Monthly Payments','Personal','Food','Entertainment','Domestic','Travels']
		cat_bill={}
		for category in categories:
			# print(Bills.objects.filter(user=request.user,billType=category))
			cat_bill[category]=Bills.objects.filter(user=request.user,billType=category)
		return cat_bill
	else: 
		return redirect(settings.LOGIN_REDIRECT_URL)




