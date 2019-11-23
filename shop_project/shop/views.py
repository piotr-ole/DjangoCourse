from django.http import HttpResponse
from django.shortcuts import render

shop_introduction = "Welcome in the shop: \"Zoo Animations For Curious Animators\"!"

def index(request):
    response_lines = ["Welcome to my Shop Project!",
                       "1. Change your URL to /shop to enter the shop.",
                       "2. Change your URL to /shop/your_name to enter your shop account."]
    return HttpResponse('<br>'.join(response_lines))


def shop(request):
    global shop_introduction
    return render(request, r'shop\main.html')

def shop_account(request, name):
    global shop_introduction
    response_lines = [shop_introduction, "Hi, " + name + "!"]
    return render(request, r'shop\client.html', {'client_name' : name})