from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'department',
        'goal_description',
        'goal_criteria',
        'rating',
        'last_update',
        'updated_at',
        'others',
        ]
    
admin.site.register(SimpleHistoryAdmin)