from django import forms
from django.forms import ModelForm

from .models import *


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class NameForm(ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

