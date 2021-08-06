from django import forms
from django.forms import ModelForm

from .models import Product, comment


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

#comment


class NameForm(ModelForm):

    class Meta:
        model = comment
        fields = '__all__'