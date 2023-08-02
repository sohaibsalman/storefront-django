from django.contrib import admin
from ..models import OrderItem

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    extra = 0
    model = OrderItem