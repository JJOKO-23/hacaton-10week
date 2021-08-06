from datetime import timedelta

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from account.models import User
from .forms import *
from .models import *

from .permissions import UserHasPermissionMixin


# def categories(request):
#     return render(request, 'index.html')
#
# def product_detail(request):
#     return render(request, 'product.html')

def blank(request):
    return render(request, 'blank.html')
#
# def store(request):
#     paginate_by = 2
#     return render(request, 'store.html')

def checkout(request):
    return render(request, 'checkout.html')
#
# def update_product(request):
#     return render(request, 'update-product.html')
#
# def add_product(request):
#     return render(request, 'add-product.html')
#
# def delete_product(request):
#     return render(request, 'delete-product.html')
#
#
#


class SearchListView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if not q:
            return Product.objects.none()
        queryset = queryset.filter(Q(name__icontains=q) |
                                   Q(description__icontains=q))
        return queryset


class CategoryListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'store.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductCategoryView(ListView):
    model = Product
    template_name = 'category.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get('slug')
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class ProductCreateView(IsAdminCheckMixin, CreateView):
    model = Product
    template_name = 'add-product.html'
    form_class = CreateProductForm


class ProductUpdateView(IsAdminCheckMixin, UpdateView):
    model = Product
    template_name = 'update-product.html'
    form_class = UpdateProductForm
    pk_url_kwarg = 'id'


class ProductDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'delete-product.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home')

#comment
def get_comment(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            # Сохранение формы
            form.save()

            # Редирект на ту же страницу
            return HttpResponseRedirect(request.path_info)

    else:
    # метод GET
        form = NameForm()
        # Получение всех имен из БД.
        comms = Comment.objects.all()
        name = request.user.username

    # И добавляем names в контекст, чтобы плучить к ним доступ в шаблоне
    return render(request, 'comm.html', {'form': form, 'comments': comms, 'name': name, "product": product})











