from django.urls import path, include

from . import views

urlpatterns = [
    path("login/", views.login_page, name="login_page"),
    path("register/", views.register_page, name="register_page"),
    path("logout/", views.logout_page, name="logout_page"),
    path("profile/<int:id>/", views.profile_page, name="profile_page"),
    path("profile/<int:id>/update/", views.update_details, name="profile_page_update_details")
]