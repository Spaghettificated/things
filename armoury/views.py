from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Product, Comment, Category


def product_list(request):
    products = get_list_or_404(Product, is_deleted=False)
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "list.html", {"products": products})

def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_deleted=False)
    comments = product.comments.all()
    # return HttpResponse(f"product #{product_id}: {product.title}")
    return render(request, "product.html", {"product": product, "comments": comments})
        
