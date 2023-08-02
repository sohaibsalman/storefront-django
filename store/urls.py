from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list),
    path('products/<int:id>/', views.product_details),
    path('collections/', views.collections_list),
    path('collections/<int:id>/', views.collection_details),
]