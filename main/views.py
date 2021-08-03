from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def categories(request):
    return render(request, 'index.html')


def product_detail(request):
    return render(request, 'product.html')


def blank(request):
    return render(request, 'blank.html')


def store(request):
    return render(request, 'store.html')


def checkout(request):
    return render(request, 'checkout.html')







