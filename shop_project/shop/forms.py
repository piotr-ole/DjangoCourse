from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'country', 'city',
                  'street', 'building_number', 'apartament_number',
                  'delivery']
