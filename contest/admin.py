from django.contrib import admin
from .models import Contest, UserContestAnswer, ContestTest
from django.contrib.admin import ModelAdmin


@admin.register(Contest)
class ContestAdmin(ModelAdmin):
    pass


@admin.register(UserContestAnswer)
class UserContestAnswerAdmin(ModelAdmin):
    pass


@admin.register(ContestTest)
class Contest_TestAnswerAdmin(ModelAdmin):
    pass
