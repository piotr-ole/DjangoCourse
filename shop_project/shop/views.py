from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

shop_introduction = "Welcome in the shop: \"Zoo Animations For Curious Animators\"!"

<<<<<<< HEAD
def index(request):
    return render(request, 'shop/index.html')
=======
products = [
    {"name": "Książka o samochodach",
     "price": 100, "id": 1, "description": "Wstęp do obsługi Malucha", "author": "Bernard Żuk"},
    {"name": "Film o helikopterach",
        "price": 50, "id": 2, "description": "Pościgi i wybuchy, w roli głównej Tomasz Karolak", "author": "Patryk Vegeta"},
    {"name": "Komiks o statkach",
        "price": 15, "id": 3, "description": "Finezyjna przygoda w świecie żeglugi", "author": "Katarzyna Gafel"},
]


def index(request):
    response_lines = ["Welcome to my Shop Project!",
                      "1. Change your URL to /shop to enter the shop and log in.",
                      "2. Change your URL to /products to browse our shop",
                      ]
    return render(request, r'shop\map.html')
>>>>>>> 16dc51202e576a786f2cd3ba931475410ad0d467


def shop(request):
    global shop_introduction
    return render(request, 'shop/main.html')


def shop_account(request, name):
    global shop_introduction
<<<<<<< HEAD
    return render(request, 'shop/client.html', {'client_name' : name})
=======
    return render(request, r'shop\client.html', {'client_name': name})

>>>>>>> 16dc51202e576a786f2cd3ba931475410ad0d467

def products_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}
    return render(request, "shop/list.html", context)



def product_details(request, product_id):
<<<<<<< HEAD
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, "shop/product_details.html", context)


=======
    global products
    return render(request, r"shop\product_details.html", {"products": products, "product_id": product_id})
>>>>>>> 16dc51202e576a786f2cd3ba931475410ad0d467
