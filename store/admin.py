from django.contrib import admin
from . import models


# Register your models here.
# Every django app has admin.py file to customize the models registering

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product: models.Product) -> str:
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
    
    def collection_title(self, product: models.Product) -> str:
        return product.collection.title


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    ordering = ['first_name', 'last_name']
    list_editable = ['membership']
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment_status', 'customer']
    ordering = ['placed_at', 'payment_status']
    list_per_page = 10
    list_select_related = ['customer']

admin.site.register(models.Collection)