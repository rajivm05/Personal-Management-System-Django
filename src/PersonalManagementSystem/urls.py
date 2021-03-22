
# from django.contrib import admin
# from django.urls import path, include
# from homeapp.views import homepage_view
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',homepage_view),

# ]
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, ChangeLanguageView
from dashboard.views import dashboard_view
from todolist.views import CreateToDoListView, taskJson, deleteJson, markItemAsCompleted, editTask
from issues.views import IssueView
from passwords.views import PasswordView, deletePassword, updatePassword
# from schedules.views import ScheduleView
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
    path('dashboard/',include('dashboard.urls')),

    path('todolist/',CreateToDoListView.as_view()),
    path('todolist/json/<int:task>',taskJson,name='taskJson'),
    path('todolist/delete/<int:task>',deleteJson,name='deleteJson'),
    path('todolist/update/<int:task>',markItemAsCompleted,name='markItemAsCompleted'),
    path('todolist/edit/<int:task>',editTask,name='editTask'),

    path('issues/',IssueView.as_view()),

    path('passwords/',PasswordView.as_view()),
    path('passwords/delete/<int:password>',deletePassword,name='deletePassword'),
    path('passwords/update/<int:password>',updatePassword,name='updatePassword'),

    # path('schedules/',ScheduleView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
