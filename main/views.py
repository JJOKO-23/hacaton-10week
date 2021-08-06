from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateProductForm, UpdateProductForm, NameForm
from .models import Product, comment
from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'main/base.html')

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'main/detail.html', {'product': product})



def create_product(request):
    if request.method == 'POST':
        product_form = CreateProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            return redirect(product.get_absolute_url())
    else:
        product_form = CreateProductForm()
    return render(request, 'main/create_product.html',
                  {'product_form': product_form})


def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product_form = UpdateProductForm(request.POST or None, request.FILES or None,
                                     instance=product)
    if product_form.is_valid():
        product_form.save()
        return redirect(product.get_absolute_url())

    return render(request, 'main/update_product.html',
                  {'product_form': product_form})


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        slug = product.category.slug
        product.delete()
        return redirect('list', slug)
    return render(request, 'main/delete_product.html', {'product': product})

#comment

def get_comment(request):

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
        comms = comment.objects.all()

    # И добавляем names в контекст, чтобы плучить к ним доступ в шаблоне
    return render(request, 'main/comm.html', {'form': form, 'names': comms})


def comment_list(request):
    commentos = comment.objects.all()
    return render(request, 'main/list.html', {'comment': commentos})