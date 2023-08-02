from typing import Any, List, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet


class InventoryFilter(admin.SimpleListFilter):
    filter_value = '<10'
    title = 'Inventory'
    parameter_name = 'inventory'

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            (self.filter_value, 'Low') # tuple, 1st value indicates the filter, 2nd is to show on UI in human understandable form
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == self.filter_value:
            return queryset.filter(inventory__lt=10)