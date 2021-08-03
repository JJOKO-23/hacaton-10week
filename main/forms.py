from datetime import datetime

from django import forms

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user', )


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('image', )

