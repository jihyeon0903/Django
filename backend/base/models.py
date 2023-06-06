from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):  #class is model
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    #one to many relationship(FK) / child element is not getting deleted when parent element is removed.
    #on_delete: default CASCADE
    name = models.CharField(
        max_length=200, null=True, blank=True)
    #null=True - empty value is stored as NULL value (database)
    #blank=True - entry value can be empty (validation)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(
        max_length=200, null=True, blank=True)
    category = models.CharField(
        max_length=200, null=True, blank=True)
    description = models.TextField(
        null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=1, null=True, blank=True)
    numReviews = models.PositiveBigIntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7,decimal_places=2, null=True, blank=True)
    countInStock = models.PositiveBigIntegerField(
        null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    #snapshot of when the product is created
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(
        max_length=200, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=1 ,null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)

class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(
        max_length=100, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    #no change until we manually update
    isDelivered = models.BooleanField(default=False)
    deliverAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)

class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.PositiveBigIntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7,decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    #order can have only one shipping address (one to one)
    #when the user cancels the order then the shipping address should be removed as well
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)
