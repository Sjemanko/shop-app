from django.shortcuts import render
from django.core.mail import send_mail
from ShoppingCart.models import OrderDetail

# Create your views here.
def send_email_notification(request):
    # send_mail('test tytul', 'test', 'cypresstests@spoko.pl', ['rawom25243@tohup.com'], fail_silently=False)
    return render(request, 'sender/index.html')

# def show_order_details(request):
#     qs = OrderDetail.objects.all()
#     print(qs)