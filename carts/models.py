from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import Customer
from store.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')
    created = models.DateTimeField(auto_now_add=True)
    ordered = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_amount(self):
        pass


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(200)]
    )

    def __str__(self):
        return f'{self.item.name} - Quantity: {self.quantity}'

    def get_total_price(self):
        return self.item.price * self.quantity
