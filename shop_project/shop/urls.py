from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('shop/', views.shop),
    path('shop/<str:name>', views.shop_account),
    path('products/', views.products_list),
    path('products/<int:product_id>', views.product_details),
    path("order/", views.order),
    path("order/<int:order_id>", views.order_details),
    path("complaint/", views.complaint),
    path("complaint/<int:complaint_id>", views.complaint_details),
    path("cart", views.cart),
    path("cart/add/", views.add_to_cart),
    path("cart/delete/", views.delete_from_cart),
    path("cart/amount_change/", views.cart_amount_change),
    path('review/add/', views.add_review)
]
