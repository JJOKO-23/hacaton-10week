from django.contrib import admin
from django.urls import path
from . import views
from .class_view import *
from .views import index, get_comment, comment_list

urlpatterns = [
    #home
    path('', index, name='home'),
    #ITS MOTHER FUCKER CRUD , SO SHUTUP AND DONT TUCH IT
    path('product/<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='create-product'),
    path('product/update/<int:id>/', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:id>/', ProductDeleteView.as_view(), name='delete_product'),


    #coment
    path('comms', get_comment, name='comment'),
    path('jopa', comment_list, name='listcomment')

]