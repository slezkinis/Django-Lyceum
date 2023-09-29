from django.urls import path, include
from .views import *

urlpatterns = [
    path('task/<task_id>', show_test),
    path('', main, name='home')
]
