from django.forms import ModelForm
from .models import Order
from .models import Complaint
from .models import Review


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'country', 'city',
                  'street', 'building_number', 'apartament_number',
                  'delivery']


class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'message']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
