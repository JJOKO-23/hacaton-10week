
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .forms import CreateProductForm, UpdateProductForm
from .models import *


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'



class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class ProductCreateView(IsAdminCheckMixin, CreateView):
    model = Product
    template_name = 'main/create_product.html'
    form_class = CreateProductForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['product_form'] = self.get_form(self.get_form_class())
    #     return context


class ProductUpdateView(IsAdminCheckMixin, UpdateView):
    model = Product
    template_name = 'main/update_product.html'
    form_class = UpdateProductForm
    pk_url_kwarg = 'id'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['product_form'] = self.get_form(self.get_form_class())
    #     return context


class ProductDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'main/delete_product.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home')



