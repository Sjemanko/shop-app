from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("<str:gender>/<str:category>/", views.product_page, name='gender_category'),
]
