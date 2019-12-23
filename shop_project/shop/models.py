from django.db import models
import pdb

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(default='brak opisu', max_length=500)
    weight = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):

    DELIVERY_CHOICES = [
        ('letter', 'letter'),
        ('package', 'package'),
        ('courier', 'courier'),
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=70)
    street = models.CharField(max_length=70)
    building_number = models.IntegerField()
    apartament_number = models.IntegerField(
        default=None, blank=True, null=True)
    delivery = models.CharField(max_length=7, choices=DELIVERY_CHOICES)
    ordered_products = models.ManyToManyField(
        "Product", through="OrderedProduct")

    def __str__(self):
        return str(self.id) + '_' + self.name + '_' + self.surname

    def get_total_price(self):
        total = 0
        # pdb.set_trace()
        ordered_products = OrderedProduct.objects.filter(order=self.id)
        for ordered_product in ordered_products:
            total += ordered_product.amount * ordered_product.product.price
        return total

    def get_product_list(self):
        products = []
        # pdb.set_trace()
        ordered_products = OrderedProduct.objects.filter(order=self.id)
        for ordered_product in ordered_products:
            products.append({'name': ordered_product.product.name,
                             'amount': ordered_product.amount, 'price': ordered_product.product.price})
        return products


class OrderedProduct(models.Model):

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)


class Complaint(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=3000)


class Review(models.Model):
    RATING_CHOICES = list(range(1, 11))
    RATING_CHOICES = [(x, x) for x in RATING_CHOICES]
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.CharField(max_length=3000)
