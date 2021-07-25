from django.urls import path
from .views import SearchProduct, product,ProductList, product_detail, ProductListByCategory, products_categories_partial
urlpatterns = [
    path('products-function', product),
    path('products',ProductList.as_view()),
    path('products/<category_name>',ProductListByCategory.as_view()),
    path('product/<productId>/<name>',product_detail),
    path('products/search',SearchProduct.as_view()),
    path('products_categories_partial',products_categories_partial,name= 'products_categories_partial')
    ]
