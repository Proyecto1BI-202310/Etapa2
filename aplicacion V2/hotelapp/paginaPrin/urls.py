from django.urls import path
from . import views

app_name = 'paginaPrin'

urlpatterns = [
    path('', views.index, name='index'),
]