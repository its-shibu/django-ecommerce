from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('app/', views.test),
    path('product/', views.show_products),
    path('addcategory/', views.post_category),
    path('addproduct/', views.post_product),
    path('category/', views.show_category),
    path('delete_category/<int:category_id>', views.delete_category),
    path('update_category/<int:category_id>', views.update_category_form),
]