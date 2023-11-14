from django.contrib import admin
from .models import userdetails, Payment, location
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# @admin.register(Payment)
class userdat(ImportExportModelAdmin):
    ...

# admin.site.register(userdat)
admin.site.register(Payment, userdat)
admin.site.register(userdetails, userdat)
admin.site.register(location)