from django.urls import path
from .views import get_Negativos
from .views import hotel_chart
from .views import get_Palabras

app_name = 'csvs'

urlpatterns = [
    path('', get_Negativos, name= 'upload-view'),
    path('chart', hotel_chart, name= 'chart-view'),
    path('negativos', get_Palabras, name= 'negs-view'),

]