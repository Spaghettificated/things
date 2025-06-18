from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Comment, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from django.urls import reverse

def product_list(request):
    products = get_list_or_404(Product, is_deleted=False)
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "list.html", {"products": products})

def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_deleted=False)
    comments = product.comments.all()
    # return HttpResponse(f"product #{product_id}: {product.title}")
    return render(request, "product.html", {"product": product, "comments": comments})

class ProductListView(ListView):
    queryset = Product.objects.filter(is_deleted=False)
    paginate_by = 3
    template_name = 'list.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CreateProductView(CreateView):
    model = Product
    fields = ['title', 'desc', 'image']
    template_name = 'armoury/product_edit.html'

    def get_success_url(self):
        return reverse('product', kwargs = {"product_id": self.object.id})

    # def get(self, request, *args, **kwargs):
    #     return HttpResponseRedirect(reverse('list'))
    #     # return HttpResponseRedirect("add_product.html")
    #     return render(request, "add_product.html")

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_deleted=False)
    product.is_deleted = True
    product.save()
    return HttpResponseRedirect(reverse("list"))


# class DeleteProductView(DeleteView):
#     pass

class ModifyProductView(UpdateView):
    model = Product
    fields = ['title', 'desc', 'image']
    template_name_suffix = '_edit'
    def get_success_url(self):
        return reverse('product', kwargs = {"product_id": self.object.id})

