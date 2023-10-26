from django.contrib import admin
from main.models import *

# Register your models here.
class AdminModelSingle(admin.ModelAdmin):
    pass


admin.site.register(Case, AdminModelSingle)
admin.site.register(Blog, AdminModelSingle)
admin.site.register(Feedback, AdminModelSingle)