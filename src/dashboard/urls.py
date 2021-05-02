from django.urls import path
app_name = 'dashboard'
from dashboard.views import dashboard_view,urlBillsPerMonth
urlpatterns = [
    path('main/', dashboard_view, name='dashboard_page'),
    path('main/year/<int:specified_year>',urlBillsPerMonth,name='specific_year'),
]
