from django.contrib import admin
from .models import *
#from django.contrib.auth.models import Users
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Users, ImportExportModelAdmin)
admin.site.register(WorkerArea, ImportExportModelAdmin)
admin.site.register(WorkerDetails, ImportExportModelAdmin)