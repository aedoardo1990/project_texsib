from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Goal


class GoalHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "department", "title"]
    history_list_display = ["department"]
    search_fields = ['title', 'department']

admin.site.register(Goal, GoalHistoryAdmin)