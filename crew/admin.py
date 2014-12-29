from django.contrib import admin
from crew.models import Crew

# Register your models here.


class CrewAdmin(admin.ModelAdmin):
        list_display            = ('first_name', 'last_name', 'nickname', 'department', 'superint', 'foreman', 'estimator', 'sales_rep')
        search_fields           = ['first_name', 'last_name', 'nickname', 'department', 'superint', 'foreman', 'estimator', 'sales_rep']




admin.site.register(Crew, CrewAdmin)

