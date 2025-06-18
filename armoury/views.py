from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def product_list(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return HttpResponse(f"product #{product_id}: {product.title}")
        
