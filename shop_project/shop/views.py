from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import OrderForm, ComplaintForm
from .models import Product, Order, Complaint, OrderedProduct

shop_introduction = "Welcome in the shop: \"Zoo Animations For Curious Animators\"!"


def index(request):
    return render(request, 'shop/index.html')


def shop(request):
    global shop_introduction
    return render(request, 'shop/main.html')


def shop_account(request, name):
    global shop_introduction
    return render(request, 'shop/client.html', {'client_name': name})


def products_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}
    return render(request, "shop/list.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, "shop/product_details.html", context)


def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    total_price = order.get_total_price()
    products = order.get_product_list()
    return render(request, "shop/order_details.html", {'total_price': total_price, 'products': products})


def order(request):
    products_to_order = _get_products_in_cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                country=form.cleaned_data['country'],
                city=form.cleaned_data['city'],
                street=form.cleaned_data['street'],
                building_number=form.cleaned_data['building_number'],
                apartament_number=form.cleaned_data['apartament_number'],
                delivery=form.cleaned_data['delivery']
            )
            order.save()

            for product in products_to_order:
                OrderedProduct(product=product, order=order, amount=1).save()
            request.session['cart'] = []
            return HttpResponseRedirect('/order/'+str(order.id))
    else:
        form = OrderForm()
    return render(request, "shop/order_form.html", {"form": form, "products": products_to_order})


def complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = Complaint(
                name=form.cleaned_data['name'],
                message=form.cleaned_data['message']
            )
            complaint.save()
            return HttpResponseRedirect('/complaint/'+str(complaint.id))
    else:
        form = ComplaintForm()
    return render(request, "shop/complaint_form.html", {"form": form})


def complaint_details(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    return render(request, "shop/complaint_details.html", {'name': complaint.name, 'message': complaint.message})


def cart(request):
    products_in_cart = _get_products_in_cart(request)
    return render(request, "shop/cart.html", {"products": products_in_cart})


def _get_products_in_cart(request):
    products_in_cart = []
    for item_id in request.session.get('cart', []):
        product = Product.objects.get(pk=item_id)
        products_in_cart.append(product)
    return products_in_cart


def add_to_cart(request):
    if request.method == "POST":
        if 'cart' not in request.session:
            request.session['cart'] = []
        request.session['cart'].append(request.POST['item_id'])
        request.session.modified = True
    return HttpResponseRedirect('/cart')
