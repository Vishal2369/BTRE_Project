from django.contrib import admin
from .models import Realtor

# Register your models here.


class realtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 20


admin.site.register(Realtor, realtorAdmin)
