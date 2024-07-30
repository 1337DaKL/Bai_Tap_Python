from django.urls import path
from . import views
app_name = "app"
urlpatterns = [
    path('', views.add_post, name='add'),
    path('ok/', views.save_post, name='save'),
]
