from django.contrib import admin
from .models import Human

# admin.site.register(Human)

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    fields = ('name','surname','year_of_birth','gender')
    # list_display = ('name','surname','year_of_birth','gender')
    def upper_case_name(self,obj):
        return (obj.name + ' ' +obj.surname).upper()

    list_display = ('upper_case_name',)
    upper_case_name.short_description = 'name'

# Register your models here.
