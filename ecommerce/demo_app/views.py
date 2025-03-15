from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages



def index(request):
    return HttpResponse("Hello, World! This is the home page of our e-commerce website.")

def test(request):
    return HttpResponse("This is the demo app.")

def show_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'demo/index.html', context)
    
def post_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'category added successfully')
            return redirect('/demo/addcategory')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to add category')
            return render(request, 'demo/addcategory.html', {
                'form': form
            })

    context = {
        'form':CategoryForm
    } 
    return render(request, 'demo/addcategory.html', context)


def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'product added successfully')
            return redirect('/demo/addproduct')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to add product')
            return render(request, 'demo/addproduct.html', {
                'form': form
            })
    context = {
        'form':ProductForm
    }
    return render(request, 'demo/addproduct.html', context)
    

def show_category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'demo/category.html', context)

def delete_category(request, category_id):
    category = Category.objects.get(id = category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'category deleted successfully')
    return redirect('/demo/category')

def update_category_form(request, category_id):
    category = Category.objects.get(id = category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'category updated successfully')
            return redirect('/demo/category')
        else:
            messages.add_message(request, messages.SUCCESS, 'Failed to update category')
            return render(request, 'demo/update_category.html', {
                'form': form
            })
    context = {
        'form': CategoryForm(instance = category)
    }
    return render(request, 'demo/update_category.html', context)