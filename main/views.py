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


class CategoryView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'

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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     slug = self.kwargs.get('slug')
    #     queryset = queryset.filter(category__slug=slug)
    #     return queryset
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category'] = self.kwargs.get('slug')
    #     return context




# class MainPageView(ListView):
#     model = Product
#     template_name = 'index.html'
#     context_object_name = 'products'
#
#
#     def get_template_names(self):
#         template_name = super(MainPageView, self).get_template_names()
#         search = self.request.GET.get('q')
#         filter = self.request.GET.get('filter')
#         if search:
#             template_name = 'search.html'
#         elif filter:
#             template_name='new.html'
#         return template_name
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         search = self.request.GET.get('q')
#         filter = self.request.GET.get('filter')
#         if search:
#             context['products'] = Product.objects.filter(Q(title__icontains=search) |
#                                                        Q(description__icontains=search))
#         elif filter:
#             start_date = timezone.now() - timedelta(days=1)
#             context['products'] = Product.objects.filter(created__gte=start_date)
#
#         else:
#             context['products'] = Product.objects.all()
#         return context



# class StoreView(DetailView):
#     model = Category
#     template_name = 'store.html'
#     context_object_name = 'store'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.slug = kwargs.get('slug', None)
#         return super().get(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.filter(category_id=self.slug)
#         return context


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'product.html'
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         image = self.get_object().get_image
#         context['images'] = self.get_object().images.exclude(id=image.id)
#         return context


# class IsAdminCheckMixin(UserPassesTestMixin):
#     pass
    # def test_func(self):
        # return self.request.user.is_authenticated and self.request.user.is_superuser



# class ProductCreateView(CreateView):
#     model = Product
#     template_name = 'add-product.html'
#     form_class = CreateProductForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product_form'] = self.get_form(self.get_form_class())
#         return context
#
#
# class ProductUpdateView(UpdateView):
#     model = Product
#     template_name = 'update-product.html'
#     form_class = UpdateProductForm
#     pk_url_kwarg = 'id'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product_form'] = self.get_form(self.get_form_class())
#         return context
#
#
# class ProductDeleteView(DeleteView):
#     model = Product
#     template_name = 'delete-product.html'
#     pk_url_kwarg = 'id'
#
#     def get_success_url(self):
#         return reverse('home')



# @login_required(login_url='login')
# def add_product(request):
#     ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
#     if request.method == 'POST':
#         product_form = ProductForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#         if recipe_form.is_valid() and formset.is_valid():
#             product = product_form.save(commit=False)
#             product.user = request.user
#             product.save()
#
#             for form in formset.cleaned_data:
#                 image = form['image']
#                 Image.objects.create(image=image, product=product)
#             return redirect(product.get_absolute_url())
#     else:
#         product_form = ProductForm()
#         formset = ImageFormSet(queryset=Image.objects.none())
#     return render(request, 'add-product.html', locals())
#
#
# def update_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.user == product.user:
#         ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
#         product_form = ProductForm(request.POST or None, instance=product)
#         formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.filter(recipe=product))
#         if product_form.is_valid() and formset.is_valid():
#             product = product_form.save()
#
#             for form in formset:
#                 image = form.save(commit=False)
#                 image.product = product
#                 image.save()
#             return redirect(product.get_absolute_url())
#         return render(request, 'update-product.html', locals())
#     else:
#         return HttpResponse('<h1>403 Forbidden</h1>')
#
#
# class DeleteProductView(UserHasPermissionMixin, DeleteView ):
#     model = Product
#     template_name = 'delete-product.html'
#     success_url = reverse_lazy('home')
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         messages.add_message(request, messages.SUCCESS, 'Successfully deleted!')
#         return HttpResponseRedirect(success_url)
#
#
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect, get_object_or_404
#
#
# from django.urls import reverse_lazy
# from django.views.generic import DeleteView
#
# from main.forms import ImageForm, ProductForm
# from main.models import Image, Product
# from django.forms import modelformset_factory
#
#
# def categories(request):
#     return render(request, 'index.html')
#
#
# def product_detail(request):
#     return render(request, 'product.html')
#
#
# def blank(request):
#     return render(request, 'blank.html')
#
#
# def store(request):
#     return render(request, 'store.html')
#
#
# def checkout(request):
#     return render(request, 'checkout.html')
# #
# @login_required(login_url='login')


#
# def add_product(request):
#     return render(request, 'update-product.html', locals())
#     ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
#     if request.method == 'POST':
#         product_form = CreateProductForm(request.POST)
#         # formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#         if product_form_form.is_valid() :
#             product = product_form.save(commit=False)
#             product.user = request.user
#             product.save()
#
#             for form in formset.cleaned_data:
#                 image = form['image']
#                 Image.objects.create(image=image)
#             return redirect(product.get_absolute_url())
#     else:
#         product_form = Product()
#         # formset = ImageFormSet(queryset=Image.objects.none())
#     return render(request, 'add-product.html', locals())
#
#
# def update_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.user == product.user:
#         ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
#         product_form = ProductForm(request.POST or None, instance=product)
#         formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.filter(recipe=product))
#         if product_form.is_valid() and formset.is_valid():
#             product = product_form.save()
#
#             for form in formset:
#                 image = form.save(commit=False)
#                 image.product = product
#                 image.save()
#         return render(request, 'update-product.html', locals())
#     else:
#         return HttpResponse('<h1>403 Forbidden</h1>')
#
#
# def delete(self, request, *args, **kwargs):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.delete()
#     return redirect('home')
#     return render(request, '')


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'main/detail.html'
#     context_object_name = 'product'
#     pk_url_kwarg = 'id'


class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated


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


















