from django.urls import path
from .views import ProductList, ProductDetail
from . import views
urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('', views.home, name='home'),
]
