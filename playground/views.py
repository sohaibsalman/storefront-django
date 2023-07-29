from django.shortcuts import render
from django.http import HttpResponse
from store.models import Collection, Customer, Order, OrderItem, Product


# Create your views here.
def index(request):
    # Customers with .com accounts
    customers = list(Customer.objects.filter(email__icontains='.com'))

    # Collection that don't have a featured product
    collections = list(Collection.objects.filter(featured_product__isnull=True))

    # Products with low inventory (less than 10)
    products = list(Product.objects.filter(inventory__lt=10))

    # Orders placed by customer id = 1
    orders = list(Order.objects.filter(customer_id=1))

    # Order items for products in collection 3
    order_items = list(OrderItem.objects.filter(product__collection__id=3))

    return render(request, "index.html", { 'customers': customers, 
                                          'collections': collections, 
                                          'products': products,
                                          'orders': orders,
                                          'order_items': order_items})