from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Comment, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from django.urls import reverse

def product_list(request):
    products = get_list_or_404(Product, is_deleted=False)
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "list.html", {"products": products})

def get_product_comments(product):
    return product.comments.all().filter(is_deleted=False)

def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_deleted=False)
    comments = get_product_comments(product)
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

    def get_form(self, form_class=None):
        form = super(CreateProductView, self).get_form(form_class)
        form.fields['image'].required = False
        return form

class CreateCommentView(CreateView):
    model = Comment
    fields = ['desc']
    template_name = 'armoury/product_edit.html'

    def get_success_url(self):
        # self.object.product = P
        return reverse('product', kwargs = {"product_id": self.object.product.id})

    def get(self, request,*args, pk,  **kwargs):
        product = get_object_or_404(Product, pk=pk, is_deleted=False)
        comments = get_product_comments(product)
        form = self.get_form()
        return render(request, "comment_edit.html", {"product": product, "comments": comments, "form": form, "comment_id": None})
    def form_valid(self, form):
        product_id = self.kwargs.get("pk")
        form.instance.product = get_object_or_404(Product, pk=product_id, is_deleted=False)
        return super().form_valid(form)
    def get_form(self, form_class=None):
        form = super(CreateCommentView, self).get_form(form_class)
        form.fields['desc'].label = "write comment"
        return form

class ModifyCommentView(CreateView):
    model = Comment
    fields = ['desc']
    template_name_suffix = '_edit'

    def get_success_url(self):
        # self.object.product = P
        return reverse('product', kwargs = {"product_id": self.object.product.id})

    def get(self, request,*args, product_id, pk,  **kwargs):
        product = get_object_or_404(Product, pk=product_id, is_deleted=False)
        comments = get_product_comments(product)
        print("access comment ", Comment.objects.get(id=pk), f" with id {pk}")
        print("in product ", product, f" with id {product.id}")
        form = self.get_form()
        return render(request, "comment_edit.html", {"product": product, "comments": comments, "form": form, "comment_id": pk, "pk": pk})
    #     # return render(request, "comment_edit.html", {"product": product, "comments": comments, "form": form, "comment_id": pk} | kwargs)
    #     return HttpResponseRedirect(reverse('issue-detail', kwargs=kwargs | {"product": product, "comments": comments, "comment_id": pk}))

    def form_valid(self, form):
        comment_id = self.kwargs.get("pk")
        comment = get_object_or_404(Comment, pk=comment_id, is_deleted=False)
        form.instance.product = comment.product
        form.instance.id = comment_id
        form.instance.created = comment.created
        form.instance.is_deleted = comment.is_deleted
        
        return super().form_valid(form)
    def get_form(self, form_class=None):
        form = super(ModifyCommentView, self).get_form(form_class)
        form.fields['desc'].label = "edit comment"
        comment_id = self.kwargs.get("pk")
        comment = get_object_or_404(Comment, pk=comment_id, is_deleted=False)
        form.fields['desc'].initial = comment.desc
        return form

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_deleted=False)
    product.is_deleted = True
    product.save()
    return HttpResponseRedirect(reverse("list"))

def delete_comment(request, pk, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, is_deleted=False)
    comment.is_deleted = True
    comment.save()
    return HttpResponseRedirect(reverse('product', kwargs = {"product_id": pk}))

# class DeleteProductView(DeleteView):
#     pass

class ModifyProductView(UpdateView):
    model = Product
    fields = ['title', 'desc', 'image']
    template_name_suffix = '_edit'
    def get_success_url(self):
        return reverse('product', kwargs = {"product_id": self.object.id})
    def get_form(self, form_class=None):
        form = super(ModifyProductView, self).get_form(form_class)
        form.fields['image'].required = False
        return form

