from typing import Any
from urllib.parse import urlencode
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.db.models.aggregates import Count
from django.utils.html import format_html
from django.urls import reverse
from .filters.inventory_filter import InventoryFilter
from . import models


# Register your models here.
# Every django app has admin.py file to customize the models registering

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]

    @admin.display(ordering='inventory')
    def inventory_status(self, product: models.Product) -> str:
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
    
    def collection_title(self, product: models.Product) -> str:
        return product.collection.title
    
    def clear_inventory(self, request, queryset: QuerySet):
        updated_count = queryset.update(inventory=0)
        self.message_user(request, f'{updated_count} products were successfully updated')


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    ordering = ['first_name', 'last_name']
    list_editable = ['membership']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders_count')
    def orders_count(self, customer: models.Customer) -> str:
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': customer.id
            })
        )
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment_status', 'customer']
    ordering = ['placed_at', 'payment_status']
    list_per_page = 10
    list_select_related = ['customer']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection: models.Collection):
        url = (
                reverse('admin:store_product_changelist') # reverse('admin:app_model_page')
                + "?"
                + urlencode({
                    'collection__id': str(collection.id)
                })
               )
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )