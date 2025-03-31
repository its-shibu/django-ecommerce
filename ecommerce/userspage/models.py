from django.db import models
from demo_app.models import *
from django.contrib.auth.models import User

class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
