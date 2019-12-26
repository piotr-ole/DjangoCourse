from django.forms import ModelForm
from django import forms
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
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Complaint
        fields = ['name']


class ReviewForm(ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Review
        fields = ['rating']
