from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


def chuanhoa(u):
    s = str(u)
    dem = 0
    ss = ""
    for i in range(len(s) - 1, -1, -1):
        if dem % 3 == 2 and i != 0:
            ss = ss + s[i] + '.'
        else:
            ss = ss + s[i]
        dem += 1
    ss = "".join(reversed(ss))
    return ss


class Product(models.Model):
    phanloai = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def chprice(self):
        return chuanhoa(self.price)

    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_items(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total

    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return chuanhoa(total)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        if self.product is None:
            print("Product is None for cart item:", self.id)
            return 0
        total = self.product.price * self.quantity
        return total

    def gett_total(self):
        if self.product is None:
            print("Product is None for cart item:", self.id)
            return 0
        total = self.product.price * self.quantity
        total = self.product.price * self.quantity
        return chuanhoa(total)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=10, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
