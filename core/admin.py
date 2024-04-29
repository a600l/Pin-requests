from django.contrib import admin
from .models import RequestModel

@admin.register(RequestModel)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'order_id', 'pnr', 'created_at', 'created_by', 'representative_name')  # Include 'representative_name' in list display
    search_fields = ('order_id', 'pnr', 'representative_name')  # Add 'representative_name' to searchable fields
