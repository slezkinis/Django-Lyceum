from django.urls import path, include
from .views import *

urlpatterns = [
    path('task/<task_id>', show_test),
    path('answer/<answer_id>', get_answer_status),
    path('', main, name='home')
]
