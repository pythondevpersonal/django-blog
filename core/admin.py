from django.contrib import admin
from core.models import Core

# Register your models here.
class CoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Core,CoreAdmin)