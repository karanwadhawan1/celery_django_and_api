from django.contrib import admin
from .models import Employee,DataExcel,error


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone','position','address','age']
    
@admin.register(DataExcel)
class DataExcelAdmin(admin.ModelAdmin):
    list_display=['excel_file']
    
@admin.register(error)
class DataExcelAdmin(admin.ModelAdmin):
    list_display=['error_key','error']