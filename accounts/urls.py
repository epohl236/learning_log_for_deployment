"""Defines URL patterns for the accounts application"""

from django.urls import path, include

from . import views


app_name = "accounts"
urlpatterns = [
    # Include default auth urls
    path ("", include ("django.contrib.auth.urls")),
    # Registration page
    path ("register/", views.register, name="register"),
]
