from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import OrderForm, ComplaintForm, ReviewForm
from .models import Product, Order, Complaint, OrderedProduct, Review, Discount
import pdb
from statistics import mean

shop_introduction = "Welcome in the shop: \"Zoo Animations For Curious Animators\"!"

###### BASE #######

def index(request):
    return render(request, 'shop/index.html')


def shop(request):
    global shop_introduction
    return render(request, 'shop/main.html')


def shop_account(request, name):
    global shop_introduction
    return render(request, 'shop/client.html', {'client_name': name})

###### PRODUCTS ########

def products_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}
    return render(request, "shop/list.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = list(Review.objects.all())
    reviews = [review for review in reviews if review.product.id == product_id]
    form = ReviewForm()
    context = {'product': product,
               'reviews': reviews, 'form': form,
               'mean_rating': mean_rating(reviews)}
    return render(request, "shop/product_details.html", context)


def mean_rating(reviews):
    if reviews != []:
        return f"{round(mean([r.rating for r in reviews]), 2)} / 10"
    else:
        return 'No ratings so far'

####### ORDER ########

def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    total_price = order.get_total_price()
    products = order.get_product_list()
    discount = order.get_discount()
    return render(request, "shop/order_details.html", {'total_price': total_price, 'products': products,
                                                       'discount': f"{discount}%",
                                                       "final_price": total_price * (100 - discount) / 100})


def order(request):
    products_to_order = _get_products_in_cart(request)
    products = zip(products_to_order.keys(),
                   products_to_order.values())  # keys: product_ids, values : amounts
    total_price = _cart_total_price(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if _is_discount_object(request.POST['discount']) != True:
            return render(request, "shop/order_form.html", {"form": form, "products": products,
                                                            "total_price": total_price,
                                                            "discount_message": "The code is not valid"})
        if form.is_valid():
            order = Order(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                country=form.cleaned_data['country'],
                city=form.cleaned_data['city'],
                street=form.cleaned_data['street'],
                building_number=form.cleaned_data['building_number'],
                apartament_number=form.cleaned_data['apartament_number'],
                delivery=form.cleaned_data['delivery'],
                discount=_get_discount_object(request.POST['discount'])
            )
            order.save()

            for product, amount in products:
                OrderedProduct(product=product, order=order,
                               amount=amount).save()
            request.session['cart'] = dict()
            return HttpResponseRedirect('/order/'+str(order.id))
    else:
        form = OrderForm()
    return render(request, "shop/order_form.html", {"form": form, "products": products,
                                                    "total_price": total_price, "discount_message": ""})


def _is_discount_object(discount_pk):
    try:
        discount = Discount.objects.get(pk=discount_pk)
        return True
    except Discount.DoesNotExist:
        if discount_pk == 'Type a discount code' or discount_pk == '':
            return True
        return False


def _get_discount_object(discount_pk):
    try:
        discount = Discount.objects.get(pk=discount_pk)
        return discount
    except Discount.DoesNotExist:
        return Discount.objects.get(pk='EMPTY') # 0% 'EMPTY' code in Discount table

####### COMPLAINT ########


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

###### CART #######


def cart(request):
    products_in_cart = _get_products_in_cart(request)
    products = zip(products_in_cart.keys(), products_in_cart.values())
    price_total = _cart_total_price(request)
    return render(request, "shop/cart.html", {"products": products, "price_total": price_total})


def _get_products_in_cart(request):
    products_in_cart = dict()
    cart_dict = request.session.get('cart', dict())
    for item_id in cart_dict.keys():
        product = Product.objects.get(pk=item_id)
        products_in_cart[product] = cart_dict[item_id]
    return products_in_cart


def add_to_cart(request):
    if request.method == "POST":
        if 'cart' not in request.session:
            request.session['cart'] = dict()
        # Dict:: keys: products_ids, values: amounts)
        product_id = request.POST['item_id']
        if product_id in request.session['cart'].keys():
            request.session['cart'][product_id] += 1
        else:
            request.session['cart'][product_id] = 1
        request.session.modified = True
    return HttpResponseRedirect('/cart')


def delete_from_cart(request):
    if request.method == "POST":
        del request.session['cart'][request.POST['item_id']]
        request.session.modified = True
    return HttpResponseRedirect('/cart')


def cart_amount_change(request):
    if request.method == "POST":
        request.session['cart'][request.POST['product_id']] = int(
            request.POST['amount'])
        request.session.modified = True
    return HttpResponseRedirect('/cart')


def _cart_total_price(request):
    products_in_cart = _get_products_in_cart(request)
    products = zip(products_in_cart.keys(), products_in_cart.values())
    price_total = 0
    for product, amount in products:
        price_total += product.price * amount
    return price_total

###### REVIEW ######


def add_review(request):
    # POST ONLY
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                product=Product.objects.get(pk=request.POST['product_id']),
                rating=form.cleaned_data['rating'],
                comment=form.cleaned_data['comment']
            )
            review.save()
    return HttpResponseRedirect('/products/' + str(request.POST['product_id']))
