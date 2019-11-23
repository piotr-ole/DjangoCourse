from django.http import HttpResponse
from django.shortcuts import render

shop_introduction = "Welcome in the shop: \"Zoo Animations For Curious Animators\"!"

products = [
 {"name": "Książka o samochodach",
"price": 100, "id": 1, "description": "Wstęp do obsługi Malucha", "author" : "Bernard Żuk"},
 {"name": "Film o helikopterach",
"price": 50, "id": 2, "description": "Pościgi i wybuchy, w roli głównej Tomasz Karolak", "author" : "Patryk Vegeta"},
 {"name": "Komiks o statkach",
"price": 15, "id": 3, "description": "Finezyjna przygoda w świecie żeglugi", "author" : "Katarzyna Gafel"},
]

def index(request):
    response_lines = ["Welcome to my Shop Project!",
                       "1. Change your URL to /shop to enter the shop and log in.",
                       "2. Change your URL to /products to browse our shop",
                       ]
    return HttpResponse('<br>'.join(response_lines))


def shop(request):
    global shop_introduction
    return render(request, r'shop\main.html')

def shop_account(request, name):
    global shop_introduction
    return render(request, r'shop\client.html', {'client_name' : name})

def products_list(request):
    global products
    return render(request, r"shop\list.html", {"products": products})

def product_details(request, product_id):
    global products
    return render(request, r"shop\product_details.html", {"products": products , "product_id" : product_id})