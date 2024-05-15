from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Goal


admin.site.register(Goal, SimpleHistoryAdmin)

