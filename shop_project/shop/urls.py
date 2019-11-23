from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('shop/', views.shop),
    path('shop/<str:name>', views.shop_account),
    path('products/', views.products_list),
    path('products/<int:product_id>', views.product_details)
]