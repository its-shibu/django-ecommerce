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
def order_items(request, product_id, cart_id):
    user = request.user
    product = Product.objects.get(id = product_id)
    cart = Cart.objects.get(id = cart_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            price = product.product_price
            total_price = int(quantity) * int(price)
            contact_no = request.POST.get('contact_no')
            address = request.POST.get('address')
            payment_method = request.POST.get('payment')
            payment_status = request.POST.get('payment_status')
            status = request.POST.get('status')
            order = Order.objects.create(
                user=user,
                product=product,
                cart=cart,
                quantity=quantity,
                total_price=total_price,
                contact_no=contact_no,
                address=address,
                payment_method=payment_method,
                payment_status=payment_status,
                status=status
            )
            if order.payment_method == 'Cash on Delivery':
                cart = Cart.objects.get(id=cart_id)
                cart.delete()
                messages.add_message(request, messages.SUCCESS, 'Order placed successfully')
                return redirect('/myorders')
            elif order.payment_method == 'Esewa':
                context = {
                    'order': order,
                    'cart': order_items,
                }
                return render(request, 'client/esewa_payment.html', context)
            else:
                messages.add_message(request, messages.ERROR, 'something went wrong')
                return render(request, 'client/order.html', context)



    context = {
        'form': OrderForm

    }
    return render(request, 'client/order.html', context)