from django.contrib import admin

from main.models import *


class ImageInlaneAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInlaneAdmin,]

admin.site.register(Category)

