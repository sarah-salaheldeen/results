from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . models import Level , Student , Subject , Department , Grade

# Register your models here.
admin.site.register(Level)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Grade)


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass