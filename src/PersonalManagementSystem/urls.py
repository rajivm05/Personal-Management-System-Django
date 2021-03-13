
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
from todolist.views import CreateToDoListView, taskJson, deleteJson
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


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
