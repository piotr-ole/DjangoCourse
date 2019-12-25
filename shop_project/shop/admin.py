from django.contrib import admin
from .models import Product, Order, OrderedProduct
from .models import Complaint, Review, Discount

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedProduct)
admin.site.register(Complaint)
admin.site.register(Review)
admin.site.register(Discount)
