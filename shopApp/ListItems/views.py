from django.shortcuts import render
from .models import Product
from django.http import response
from django.shortcuts import redirect

# Create your views here.

def product_page(request, gender, category):
    return render(request, 'ListItems/product_page.html', {'gender': gender, 'category': category})

def show_all_products(request):
    products = Product.objects.all()
    products_categories = Product.ClothCategory
    if request.method == "POST":
        if 'search_button' in request.POST:
            filtered_products = filter_products_by_name(request, request.POST['name'])
            products = filtered_products
        elif 'cloth_category' in request.POST and 'filter_button' in request.POST and 'radio' in request.POST:
            filtered_products = filter_products_by_category_and_gender(request, request.POST['cloth_category'], request.POST['radio'])
            products = filtered_products
        elif 'filter_button' in request.POST and 'radio' in request.POST:
            filtered_products = filter_products_by_gender(request, request.POST['radio'])
            products = filtered_products
        elif 'cloth_category' in request.POST:
            filtered_products = filter_products_by_category(request, request.POST['cloth_category'])
            products = filtered_products
    return render(request, 'ListItems/products.html', {'item_list': products, "product_categories": products_categories })


def filter_products_by_name(request, product_name):
    filtered_products = Product.objects.filter(name__contains=product_name)
    return filtered_products

def filter_products_by_gender(request, gender):
    filtered_products = Product.objects.filter(gender=gender)
    return filtered_products

def filter_products_by_category(request, category):
    filtered_products = Product.objects.filter(cloth_category=category)
    return filtered_products

def filter_products_by_category_and_gender(request, category, gender):
    filtered_products = Product.objects.filter(cloth_category=category, gender=gender)
    return filtered_products