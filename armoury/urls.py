from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("add", views.CreateProductView.as_view(), name="add"),
    path("<int:product_id>/", views.product_page, name="product"),
    # path("<int:product_id>/delete", views.DeleteProductView.as_view(), name="delete"),
    path("<int:product_id>/delete", views.delete_product, name="delete"),
    path("<pk>/modify", views.ModifyProductView.as_view(), name="modify"),
]