from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

shop_introduction = "Welcome in the shop: \"Zoo Animations For Curious Animators\"!"

def index(request):
    return render(request, 'shop/index.html')


def shop(request):
    global shop_introduction
    return render(request, 'shop/main.html')

def shop_account(request, name):
    global shop_introduction
    return render(request, 'shop/client.html', {'client_name' : name})

def products_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}
    return render(request, "shop/list.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, "shop/product_details.html", context)


