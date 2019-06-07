# works/admin.py
from django.contrib import admin
from .  models import Work

class WorkAdmin(admin.ModelAdmin):
    readonly_fields=()

admin.site.register(Work, WorkAdmin)
