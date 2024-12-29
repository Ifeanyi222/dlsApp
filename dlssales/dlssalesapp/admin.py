from django.contrib import admin
from .models import Phone, Sale

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'stock', 'created_at']
    search_fields = ['name', 'brand']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['phone', 'quantity', 'total_price', 'date']
    list_filter = ['date']

