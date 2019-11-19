from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('shop/', views.shop),
    path('shop/<str:name>', views.shop_account)
]