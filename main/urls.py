from django.urls import path

from .views import *
from .cart import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('store/', ProductListView.as_view(), name='store'),
    path('store/<str:slug>/', ProductCategoryView.as_view(), name='category_list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('checkout/', checkout, name='checkout'),
    path('blank/', blank, name='blank'),
    path('add-product/', ProductCreateView.as_view(), name='add-product'),
    path('update-product/<int:id>/', ProductUpdateView.as_view(), name='update-product'),
    path('delete-product/<int:id>/', ProductDeleteView.as_view(), name='delete-product'),
    path('search', SearchListView.as_view(), name='search'),
    path('comments/<int:id>/', get_comment, name='comment'),

# Cart urls

    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),

]






