from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products),
    path('productdetails/<int:product_id>', views.product_details)
]