# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('otp-verification/', views.verify_otp, name='verify_otp'),
    path('otp-success/', views.otp_success, name='otp_success'),  # Define this view as needed
]
