from django.contrib import admin
from .models import Qradardb
from import_export.admin import ImportExportModelAdmin


@admin.register(Qradardb)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('logsource', 'qradar_condition')
