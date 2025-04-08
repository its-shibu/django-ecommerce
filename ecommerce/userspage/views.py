from django.shortcuts import get_object_or_404, render, redirect
from demo_app.models import *
from userspage.forms import OrderForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only


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

def product_details(request, product_id):
    product = Product.objects.get(id = product_id)
    context = {
        'product': product
    }
    return render(request, 'client/product_details.html', context)


@login_required
@user_only
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id = product_id)
    
    check_itmes_presence = Cart.objects.filter(user=user, product= product)
    if check_itmes_presence:
        messages.add_message(request, messages.ERROR, 'Product already exist in the Cart.')
        return redirect('/mycart')
    else:
        cart = Cart.objects.create(product=product, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Items added to cart')
            return redirect('/mycart')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add to cart')
            return redirect('/product')
@login_required
@user_only
def show_cart_items(request):
    user = request.user
    items = Cart.objects.filter(user=user) 
    context = {
        'items': items
    }
    return render(request, 'client/cart.html', context)


@login_required
@user_only
def order_items(request):
    context = {
        'form' : OrderForm
    }
    return render(request, 'client/order.html', context)

