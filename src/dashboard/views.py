from django.shortcuts import render
from django.shortcuts import redirect
from todolist.models import ToDoList 
from bills.models import Bills
from django.db.models import Sum
from bills.views import preprocessMonth, getCategoricalBills
import pandas as pd
import plotly.express as px 
import plotly
from django.http import HttpResponse, JsonResponse
# Create your views here.
def dashboard_view(request):	
	context={}
	if request.user.is_authenticated:
		context['years']=retrieveYears(request)
		context['billsPerMonth']=urlBillsPerMonth(request)
		context['completeVsIncompleteTasks']=plotCompletedVsIncompleteTasksPerCategory(request)
		context['topTasksToDo']=topTasksToDo(request)
		context['expenditurePerCategory']=plotExpenditureCategory(request)
		return render(request,'dashboard.html',context)
	else:
		return redirect('accounts:log_in')
def plotCompletedVsIncompleteTasksPerCategory(request):
	if request.user.is_authenticated:
		categories = ['Academic', 'Administrative','Personal', 'Research']
		task_dictionary={}
		for category in categories:
			temp_dictionary = {}
			temp_dictionary['complete'] = len(ToDoList.objects.filter(user=request.user,taskType=category,mark_as_complete=True))
			temp_dictionary['incomplete'] = len(ToDoList.objects.filter(user=request.user,taskType=category,mark_as_complete=False))
			task_dictionary[category] = temp_dictionary
		df = pd.DataFrame(task_dictionary).transpose()
		fig=px.bar(df,labels={"index":"Category","value":"Number of tasks"},barmode='group',color_discrete_sequence=["rgb(102,197,204)", "rgb(248,158,116)"])
		fig.update_layout(title_text="Completed vs Pending Tasks", title_x=0.5)
		fig.update_yaxes(tick0=0, dtick=1, ticks="outside")
		fig = plotly.offline.plot(fig, auto_open = False, output_type="div")
		return fig
	else:
		return redirect('accounts:log_in')
def topTasksToDo(request):
	if request.user.is_authenticated:
		response = ToDoList.objects.filter(user=request.user,mark_as_complete=False).order_by('-date_added')[0:10]
		return response
	else:
		return redirect('accounts:log_in')
def billsPerMonth(request):
	if request.user.is_authenticated:
		temp = Bills.objects.extra(select={'month': 'strftime("%m %Y",date)','day':'strftime("%d",date)','year':'strftime("%Y",date)'},order_by=['month','day']).values('year','month','user').order_by('month').annotate(monthlyBill = Sum('money'))
		final = preprocessMonth(temp)
		return final
	else:
		return redirect('accounts:log_in')

def plotBillsPerMonth(request,new_df):
	if request.user.is_authenticated:
		fig = px.bar(new_df,x='month',y='monthlyBill', title='Expenditure Per Month')
		fig = plotly.offline.plot(fig, auto_open = False, output_type="div")
		return fig
	else:
		return redirect('accounts:log_in')

def generateDatasetBillsPerMonth(request,specified_year):
	if request.user.is_authenticated:
		df = pd.DataFrame(billsPerMonth(request))
		df=df[df['user']==request.user.id]
		new_df=df[df['year']==str(specified_year)]
		print(new_df)
		return new_df
	else:
		return redirect('accounts:log_in')

def retrieveYears(request):
	if request.user.is_authenticated:
		li=[]
		for date in Bills.objects.filter(user=request.user).values('date'):
			li.append(int(date['date'].strftime("%Y")))
		return sorted(list(set(li)),reverse=True)

def urlBillsPerMonth(request,specified_year=2021):
	if request.user.is_authenticated:
		df=generateDatasetBillsPerMonth(request,specified_year)
		if request.is_ajax():
			return JsonResponse({'div':plotBillsPerMonth(request,df)})
		return plotBillsPerMonth(request,df)

def plotExpenditureCategory(request):
	if request.user.is_authenticated:
		cat_bill = getCategoricalBills(request)
		cat_total_dict={}
		for category, resultSet in cat_bill.items():
			cat_total_dict[category]=0
			for temp_d in resultSet.values('money'):
				cat_total_dict[category]+=temp_d['money']
		df=pd.DataFrame()
		df['Categories']=cat_total_dict.keys()
		df['Total']=cat_total_dict.values()
		fig = px.pie(df,values='Total',names='Categories',title='Total Per Category')
		fig = plotly.offline.plot(fig, auto_open = False, output_type="div")
		return fig
	else:
		return redirect('accounts:log_in')