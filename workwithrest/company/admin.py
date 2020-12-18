from django.contrib import admin
from .models import Company, OwnerCompany


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    class Meta:
        ordering = ('-id')

    list_display = 'name city website'.split()


admin.site.register(OwnerCompany)
