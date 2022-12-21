from django.contrib import admin
from .models import userdetails, Payment
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Payment)
class userdat(ImportExportModelAdmin):
    pass

admin.site.register(userdetails)