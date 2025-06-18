from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("add", views.CreateProductView.as_view(), name="add"),
    path("<int:product_id>/", views.product_page, name="product"),
    # path("<int:product_id>/delete", views.DeleteProductView.as_view(), name="delete"),
    path("<int:product_id>/delete", views.delete_product, name="delete"),
    path("<pk>/modify", views.ModifyProductView.as_view(), name="modify"),
    path("<pk>/comment/add", views.CreateCommentView.as_view(), name="add_comment"),
    path("<pk>/comment/delete/<comment_id>", views.delete_comment, name="delete_comment"),
    path("<product_id>/comment/modify/<pk>", views.ModifyCommentView.as_view(), name="modify_comment"),
]