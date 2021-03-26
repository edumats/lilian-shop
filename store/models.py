from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=120, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=False, help_text='Product can be sold')
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    featured_product = models.BooleanField(
        default=False,
        help_text='Product will appear in featured section'
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={
            'slug': self.slug
        })


class Hantem(Product):
    SIZES = [
        ('PP', 'Extra Pequeno'),
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
        ('GG', 'Extra Grande')
    ]
    size = models.CharField(max_length=2, choices=SIZES)


class ProductImage(models.Model):
    pass
