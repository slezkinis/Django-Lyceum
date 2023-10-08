from django.contrib import admin
from .models import Contest, UserContestAnswer, ContestTest
from django.contrib.admin import ModelAdmin



@admin.register(Contest)
class ContestAdmin(ModelAdmin):
    fields = ('name', 'description', 'input_data', 'output_data', 'for_everyone', 'special_for_users', 'id')
    readonly_fields = ('id', )

    def id(self, obj):
        return obj.id
    

@admin.register(UserContestAnswer)
class UserContestAnswerAdmin(ModelAdmin):
    pass


@admin.register(ContestTest)
class Contest_TestAnswerAdmin(ModelAdmin):
    pass
