from django.db import models


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', related_name='children',
                               null=True, blank=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title


class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии'),
        ('awaiting', 'Ожидается')
    )
    COLOR_CHOICES = (
        ('red', 'красный'),
        ('blue', 'голубой'),
        ('Black', 'черный'),
        ('grey', 'серый')
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=20)
    color = models.CharField(choices=COLOR_CHOICES,
                             max_length=20)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', kwargs={'id': self.pk})

    class Meta:
        ordering = ['name']


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url


class Comment(models.Model):
    body = models.TextField()

    def __str__(self):
        return 'Comment by {} '.format(self.name)



