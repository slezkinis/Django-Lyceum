from django.contrib import admin
from .models import Contest, UserContestAnswer, ContestTest, ContestGroup
from django.contrib.admin import ModelAdmin
from django.urls import reverse
# from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class ContestInline(admin.TabularInline):
    model = ContestTest
    fields = ['input', 'answer']
    extra = 0

@admin.register(Contest)
class ContestAdmin(ModelAdmin):
    fields = ('name', 'description', 'input_data', 'output_data', 'type_programm', 'timeout', 'for_everyone', 'special_for_users', 'id')
    readonly_fields = ('id', )
    inlines = [
        ContestInline
    ]

    def id(self, obj):
        return obj.id
    

@admin.register(UserContestAnswer)
class UserContestAnswerAdmin(ModelAdmin):
    list_filter=['user', 'contest']
    search_fields=['short_status']
    list_display=['get_str', 'user', 'short_status']
    def get_str(self, obj):
        return f'{obj.user.username}_{obj.contest.name}_{obj.id}'


@admin.register(ContestTest)
class Contest_TestAnswerAdmin(ModelAdmin):
    list_filter=('contest', )

@admin.register(ContestGroup)
class ContestGroupAdmin(ModelAdmin):
    search_fields=['name']
    fields = ('name', 'contests', 'text_to_users', 'special_for_users', 'id', 'customer_link')
    readonly_fields = ('id', 'customer_link')

    def id(self, obj):
        return obj.id

    def customer_link(self, obj):
        return u'{0}'.format(reverse('group', args=(obj.id, )))