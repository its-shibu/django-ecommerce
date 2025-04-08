from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products),
    path('productdetails/<int:product_id>', views.product_details),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name = 'add_to_cart'),
    path('mycart/', views.show_cart_items, name= 'show_cart_items'),
    path('order_items/',views.order_items, name='order_items'),
    ]