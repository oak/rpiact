from django.contrib import admin

# Register your models here.
from web.models import Action, Execution

admin.site.register(Action, admin.ModelAdmin)
admin.site.register(Execution, admin.ModelAdmin)