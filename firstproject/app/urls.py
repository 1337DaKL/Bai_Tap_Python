
from django.urls import path
from . import views
from .views import IndexView
urlpatterns = [
    path('', views.index, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout/pay/', IndexView.as_view()),
    path('ao/', views.showallao, name="showao"),
    path('quan/', views.showallquan, name="showquan"),
    path('giay/', views.showallgiay, name="showgiay"),
    path('non/', views.showallnon, name="shownon"),
    path('register/', views.register, name="register"),
]
