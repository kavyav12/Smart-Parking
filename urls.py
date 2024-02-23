from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('parking_availability/', views.parking_availability, name='parking_availability'),
    path('register/', views.register, name='register'),
    path('pre_booking/', views.pre_booking, name='pre_booking'),
    path('pre-booking/submit/', views.pre_booking_submit, name='pre_booking_submit'),
    path('payment/', views.payment, name='payment'),

]
