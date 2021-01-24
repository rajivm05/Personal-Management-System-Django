from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
def dashboard_view(request):	
	context={}
	if request.user.is_authenticated:
		return render(request,'dashboard.html',context)
	else:
		return redirect('accounts:log_in')
	