from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages
import os
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only



def index(request):
    return HttpResponse("Hello, World! This is the home page of our e-commerce website.")

def test(request):
    return HttpResponse("This is the demo app.")

@login_required
@admin_only
def show_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'demo/index.html', context)
    

@login_required    
@admin_only
def post_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'category added successfully')
            return redirect('/admin/addcategory')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to add category')
            return render(request, 'demo/addcategory.html', {
                'form': form
            })

    context = {
        'form':CategoryForm
    } 
    return render(request, 'demo/addcategory.html', context)

@login_required
@admin_only
def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'product added successfully')
            return redirect('/admin/addproduct')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to add product')
            return render(request, 'demo/addproduct.html', {
                'form': form
            })
    context = {
        'form':ProductForm
    }
    return render(request, 'demo/addproduct.html', context)
    
@login_required
@admin_only
def show_category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'demo/category.html', context)


@login_required
@admin_only
def delete_category(request, category_id):
    category = Category.objects.get(id = category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'category deleted successfully')
    return redirect('/admin/category')


@login_required
@admin_only
def update_category_form(request, category_id):
    category = Category.objects.get(id = category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'category updated successfully')
            return redirect('/admin/category')
        else:
            messages.add_message(request, messages.SUCCESS, 'Failed to update category')
            return render(request, 'demo/update_category.html', {
                'form': form
            })
    context = {
        'form': CategoryForm(instance = category)
    }
    return render(request, 'demo/update_category.html', context)


@login_required
@admin_only
def delete_product(request, product_id):
    product = Product.objects.get(id = product_id)
    os.remove(product.product_image.path)
    product.delete()
    messages.add_message(request, messages.SUCCESS, 'product deleted successfully')
    return redirect('/admin/product')


@login_required
@admin_only

def update_product_form(request, product_id):
    product = Product.objects.get(id = product_id)
    if request.method == "POST":
        if request.FILES:
            os.remove(product.product_image.path)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'product updated successfully')
            return redirect('/admin/product')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to update product')
            return render(request, 'demo/update_product.html', {
                'form': form
            })
    context = {
        'form': ProductForm(instance=product)
    }
    return render(request, 'demo/update_product.html', context)
        