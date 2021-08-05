from django.contrib import admin
from django.urls import path
from . import views
from .class_view import *
from .views import index



urlpatterns = [
    path('', index, name='home'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='create-product'),
    path('product/update/<int:id>/', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:id>/', ProductDeleteView.as_view(), name='delete_product'),
]