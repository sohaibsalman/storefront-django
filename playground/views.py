from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
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

    # Logical AND operation using filter multiple args
    logical_and = Product.objects.filter(unit_price=10, inventory__lt=20)

    # Logical AND using chaining filter
    logical_and_chaining = Product.objects.filter(unit_price=10).filter(inventory__lt=20)

    # Logical OR using Q function
    logical_or = Product.objects.filter(Q(unit_price=10) | Q(unit_price=20))

    # Logical NOT using Q function
    logical_not = Product.objects.filter(Q(unit_price=10) | ~Q(inventory__lt=20))

    # Filtering using Reference fields (to compare 1 field/column with another)
    reference_field = Product.objects.filter(inventory=F('collection__id'))

    # Sorting
    sorting = Product.objects.order_by('unit_price', '-title')
    earliest = Product.objects.earliest('title')
    latest = Product.objects.latest('title')

    # Limit customer
    customers = list(Customer.objects.all()[:5])

    # Select product which has been ordered
    products = Product.objects.filter(id__in=
        OrderItem.objects.values('product_id').distinct()
    ).order_by('title')

    return render(request, "index.html", { 'customers': customers, 
                                          'collections': collections, 
                                          'products': products,
                                          'orders': orders,
                                          'order_items': order_items})