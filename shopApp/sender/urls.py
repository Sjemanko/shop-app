from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.send_email_notification, name="send_email_notification"),
    # path("show-order-details/", views.show_order_details, name="show_order_details")
]