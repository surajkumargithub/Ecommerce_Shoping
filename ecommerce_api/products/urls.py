from django.urls import path
from .views import ProductList, ProductDetail
from .views import product_list

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('', product_list, name='product_list'),
]
