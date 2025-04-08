from django.db import models
from demo_app.models import *
from django.contrib.auth.models import User

class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
class Order(models.Model):
    PAYMENT = (
        ('Cash on Delivery', 'Cash on Delivery'),
        ('Esewa', 'Esewa'),
        ('Khalti', 'Khalti'),
    )
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField(null = True)
    status = models.CharField(max_length=100, default='Pending')
    payment = models.CharField(max_length=100, choices=PAYMENT, default='Cash on Delivery')
    payment_status = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    oreder_date = models.DateTimeField(auto_now_add=True)
    