from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


# We can combine multiple view using a view set
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitem_set.count() > 0:
            return Response({'error': 'Cannot delete a product associated with order item'}, status=status.HTTP_400_BAD_REQUEST)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(self.queryset, pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Cannot delete a collection having products'}, status=status.HTTP_400_BAD_REQUEST)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.select_related('collection').all()
#     serializer_class = ProductSerializer


# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def delete(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         if product.orderitem_set.count() > 0:
#             return Response({'error': 'Cannot delete a product associated with order item'}, status=status.HTTP_400_BAD_REQUEST)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.annotate(products_count=Count('products'))
#     serializer_class = CollectionSerializer


# class CollectionDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.annotate(products_count=Count('products'))
#     serializer_class = CollectionSerializer

#     def delete(self, request, pk):
#         collection = get_object_or_404(Collection.objects.annotate(products_count=Count('products')), pk=pk)
#         if collection.products.count() > 0:
#             return Response({'error': 'Cannot delete a collection having products'}, status=status.HTTP_400_BAD_REQUEST)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def products_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_details(request, id):
#     product = get_object_or_404(Product, pk=id)

#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         if product.orderitem_set.count() > 0:
#             return Response({'error': 'Cannot delete a product associated with order item'}, status=status.HTTP_400_BAD_REQUEST)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def collections_list(request):
#     if request.method == 'GET':
#         queryset = Collection.objects.annotate(products_count=Count('products')).all()
#         serializer = CollectionSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_details(request, id):
#     collection = get_object_or_404(Collection.objects.annotate(products_count=Count('products')), pk=id)
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CollectionSerializer(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         if collection.products.count() > 0:
#             return Response({'error': 'Cannot delete a collection having products'}, status=status.HTTP_400_BAD_REQUEST)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
