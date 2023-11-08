from django.urls import path, include
from .views import *

urlpatterns = [
    path('task/<task_id>', show_test, name='task'),
    path('answer/<answer_id>', get_answer_status),
    path('contest/<group_id>', show_contest, name='group'),
    path('', main, name='home')
]
