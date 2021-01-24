from django.urls import path
app_name = 'dashboard'
from dashboard.views import dashboard_view
urlpatterns = [
    path('main/', dashboard_view, name='dashboard_page'),
]
