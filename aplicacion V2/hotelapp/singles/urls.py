from django.urls import path
from . import views

app_name = 'singles'

urlpatterns = [
    path('', views.ingresar, name='ingresar'),
    path('result/', views.result, name='result'),
]