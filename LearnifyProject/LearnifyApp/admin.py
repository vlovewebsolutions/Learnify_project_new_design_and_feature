from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import AddStudent, ResultClassIX, ResultClassX, \
    ResultClassXI_JEE_MAIN, ResultClassXI_JEE_ADVANCE_P1, ResultClassXI_JEE_ADVANCE_P2, \
    ResultClassXII_JEE_ADVANCE_P1, ResultClassXII_JEE_ADVANCE_P2, ResultClassXII_JEE_MAIN, FeesStructure, FeeReceipt

# Register your models here.
admin.site.site_header = "Learnify Admin Panel"
admin.site.index_title = "Welcome to admin panel"
admin.site.site_title = "Learnify admin panel"


@admin.register(AddStudent)
class AddStudentAdmin(ImportExportModelAdmin):
    pass


@admin.register(ResultClassIX)
class ResultClassIXAdmin(ImportExportModelAdmin):
    pass


@admin.register(ResultClassX)
class ResultClassXAdmin(ImportExportModelAdmin):
    pass


@admin.register(ResultClassXI_JEE_MAIN)
class ResultClassXI_JEE_MAINAdmin(ImportExportModelAdmin):
    pass


@admin.register(ResultClassXII_JEE_MAIN)
class ResultClassXII_JEE_MAINAdmin(ImportExportModelAdmin):
    pass


@admin.register(ResultClassXI_JEE_ADVANCE_P1)
class ResultClassXI_JEE_ADVANCE_P1Admin(ImportExportModelAdmin):
    pass


@admin.register(ResultClassXI_JEE_ADVANCE_P2)
class ResultClassXI_JEE_ADVANCE_P2Admin(ImportExportModelAdmin):
    pass


@admin.register(ResultClassXII_JEE_ADVANCE_P1)
class ResultClassXII_JEE_ADVANCE_P1Admin(ImportExportModelAdmin):
    pass


@admin.register(ResultClassXII_JEE_ADVANCE_P2)
class ResultClassXII_JEE_ADVANCE_P2Admin(ImportExportModelAdmin):
    pass


@admin.register(FeeReceipt)
class FeeReceiptsAdmin(ImportExportModelAdmin):
    pass


@admin.register(FeesStructure)
class FeesStructureAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('year_session', 'first_session_fee',
                    'second_session_fee', 'third_session_fee',
                    'fourth_session_fee')
