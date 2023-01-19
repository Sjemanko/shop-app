from django.shortcuts import render
from .models import Product, Recommendation
from django.http import response
from django.shortcuts import redirect
from .forms import RecommendationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

def product_details_page(request, slug):
    product = Product.objects.get(slug=slug)
    recommendations = Recommendation.objects.filter(product_id=product)
    all_recomendations = recommendations.count()
    avg_score = count_average_opinion_value(request, recommendations)
    return render(request, 'ListItems/product_details.html', {"product_details": product, "recommendations": recommendations, "all_recomendations": all_recomendations,  "average_score": avg_score})

@login_required(login_url="/account/login")
def add_opinion(request, slug):
    submitted = False
    product = Product.objects.get(slug=slug)
    if request.method == "POST":
        form = RecommendationForm(request.POST)
        author = request.user
        product_id = product
        title = request.POST['title']
        content = request.POST['content']
        rating = request.POST['rating']   
        recommendation = Recommendation(title=title, content=content, product_id=product_id, rating=rating, author=author)    
        if form.is_valid(): 
            recommendation.save()
            messages.success(request, f"Your opinion has been added.")
            return HttpResponseRedirect(f'/products/{slug}/')
        else:
            messages.error(request, f"Form is not valid. Check form and correct fields.")
    else:
        form = RecommendationForm
    return render(request, "ListItems/add_opinion.html", {"form": form})

def count_average_opinion_value(request, recommendations):
    total_score = 0
    if recommendations.count() != 0:
        for recommendation in recommendations:
            total_score += recommendation.rating
        return round(total_score / recommendations.count(), 1)
    else:
        return 0
