from django.urls import path

from .views import *

urlpatterns = [
    path('', categories, name='home'),
    path('product/', product_detail, name='product_detail'),
    path('checkout/', checkout, name='checkout'),
    path('store/', store, name='store'),
    path('blank/', blank, name='blank'),
]