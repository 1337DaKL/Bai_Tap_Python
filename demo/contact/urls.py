from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path('', views.show, name='contact'),
    path('/getcontact/', views.getcontact, name="getcontact")
]
