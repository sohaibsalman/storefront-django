from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tag.models import TagItem

class TagItemInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TagItem

class CustomProductAdmin(ProductAdmin):
    inlines = [TagItemInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)