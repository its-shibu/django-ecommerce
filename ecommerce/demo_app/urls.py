from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('app/', views.test),
    path('show_product/', views.show_products),
    path('addcategory/', views.post_category),
    path('addproduct/', views.post_product),
]