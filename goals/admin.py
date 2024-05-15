from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Goal


class GoalHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'department', 'goal_description', 'goal_criteria', 'rating', 'last_update', 'others']
    history_list_display = ['department', 'goal_description', 'goal_criteria', 'rating', 'last_update', 'others']
    search_fields = ['department', 'goal_description', 'goal_criteria', 'rating', 'last_update', 'others']

admin.site.register(Goal, GoalHistoryAdmin)