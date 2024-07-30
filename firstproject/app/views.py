from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import View
from django.contrib.auth.forms import UserCreationForm


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app/home.html', context)
# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'app/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':  0}
    context = {'items': items, 'order': order}
    return render(request, 'app/checkout.html', context)


def showallao(request):
    ok = Product.objects.filter(phanloai="AO")
    context = {
        'ok': ok
    }
    return render(request, "app/ao.html", context)


def showallquan(request):
    ok = Product.objects.filter(phanloai="QUAN")
    context = {
        'ok': ok
    }
    return render(request, "app/quan.html", context)


def showallgiay(request):
    ok = Product.objects.filter(phanloai="GIAY")
    context = {
        'ok': ok
    }
    return render(request, "app/giay.html", context)


def showallnon(request):
    ok = Product.objects.filter(phanloai="NON")
    context = {
        'ok': ok
    }
    return render(request, "app/non.html", context)


class IndexView(View):
    def post(self, request):
        data1 = request.POST['name']
        data2 = request.POST['email']
        data3 = request.POST['address']
        data4 = request.POST['city']
        data5 = request.POST['state']
        data6 = request.POST['mobile']
        ShippingAddress.objects.create(
            address=data3, city=data4, state=data5, mobile=data6)
        return render(request, 'app/notification.html')


def register(request):  
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'app/register.html', context)
