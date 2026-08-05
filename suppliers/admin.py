from django.contrib import admin
from .models import Suppliers

# Register your models here.
@admin.register(Suppliers)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',  'created_at', 'updated_at', 'email', 'address')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')