from django.shortcuts import render
from demo_app.models import *


def index(request):
    products = Product.objects.all().order_by('-id')[:8]
    context = {
        'products': products
    }
    return render(request, 'client/homepage.html', context)

def products(request):
    products = Product.objects.all().order_by('-id')[:8]
    context = {
        'products': products
    }
    return render(request, 'client/products.html', context)