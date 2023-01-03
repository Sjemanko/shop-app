from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request, 'login/login_page.html')

def register_page(request):
    return render(request, 'login/register_page.html')