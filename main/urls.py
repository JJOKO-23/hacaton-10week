from django.urls import path

from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('', categories),
    path('product/', product_detail),
    path('checkout/', checkout),
    path('store/', store),
    path('blank/', blank),
=======
    path('', index),
>>>>>>> 010f106998a13b8b0d9f057908da31726c0af9d9
]