from django.contrib import admin
from .models import userdetails, Payment, location, loan
from import_export.admin import ImportExportModelAdmin, ImportMixin
# Register your models here.

# @admin.register(Payment)
class userdat(ImportExportModelAdmin, ImportMixin):
    pass

# admin.site.register(userdat)
admin.site.register(Payment, userdat)
admin.site.register(loan, userdat)
admin.site.register(userdetails, userdat)
admin.site.register(location, userdat)


# records = Payment.objects.all()
# records.delete() 