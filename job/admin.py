from django.contrib import admin
from job.models import Job, Department

# Register your models here.

class JobAdmin(admin.ModelAdmin):
	prepopulated_fields 	= {'slug': ('job_number',)}	
	list_display 		= ('job_number', 'job_date', 'department', 'level', 'job_name', 'city')
	search_fields		= ['job_number', 'job_date', 'department', 'level', 'job_name', 'city']

class DepartmentAdmin(admin.ModelAdmin):
	prepopulated_fields     = {'slug': ('name',)}


admin.site.register(Job, JobAdmin)
admin.site.register(Department, DepartmentAdmin)

