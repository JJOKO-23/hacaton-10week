from django.urls import path

from .views import *

urlpatterns = [
    path('', categories),
    path('product/', product_detail),
    path('checkout/', checkout),
    path('store/', store),
    path('blank/', blank),
]