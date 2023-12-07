from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from contest.views import view_account

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('account/', TemplateView.as_view(template_name='account.html'), name='account'),
    path('account/', view_account, name='account'),
    path('', include('contest.urls')),
    path('users/', include('users.urls')),
]
