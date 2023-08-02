from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def products_list(request):
    return Response('Ok')


@api_view()
def product_details(request, id):
    return Response(id)