from django.apps import AppConfig
from django.apps import apps
from django.contrib import admin


class GoalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goals'


HistoricalCustomModel = apps.get_model("goals", "HistoricalCustomModel")

@admin.register(HistoricalCustomModel)
class HistoricalCustomModelAdmin(admin.ModelAdmin):
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