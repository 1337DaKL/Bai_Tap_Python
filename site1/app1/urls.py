from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns here
    path('/1', views.index1, name='index1'),
    path('/out', views.getout, name='getout')
]
