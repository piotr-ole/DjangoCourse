from django.db import models

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
    apartament_number = models.IntegerField(default=None, blank=True, null=True)
    delivery = models.CharField(max_length=7, choices=DELIVERY_CHOICES)

    def __str__(self):
        return str(self.id) + '_' + self.name + '_' + self.surname