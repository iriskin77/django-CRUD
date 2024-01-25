
from django.contrib import admin
from django.urls import path
from .views import ProductsList, UpdateProduct, DeleteProduct, DetailProduct, AddProductView, ProductFilter

urlpatterns = [
    path("admin/", admin.site.urls),
    path("list_products/", ProductsList.as_view(), name='list_products'),
    path("search_products/", ProductFilter.as_view(), name="search_products"),
    path("add_product/", AddProductView.as_view(), name='add_product'),
    path("product_detail/<int:pk>", DetailProduct.as_view(), name="product_detail"),
    path("update_product/<int:pk>", UpdateProduct.as_view(), name='update_product'),
    path("delete_product/<int:pk>", DeleteProduct.as_view(), name="delete_product"),
]
