from django.contrib import admin
from .models import Product
from .models import Order
from .models import OrderedProduct
from .models import Complaint

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedProduct)
admin.site.register(Complaint)