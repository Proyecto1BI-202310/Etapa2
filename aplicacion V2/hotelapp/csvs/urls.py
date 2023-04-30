from django.urls import path
from .views import upload_file_view

app_name = 'comentarios'

urlpatterns = [
    path('', upload_file_view, name= 'upload-view'),
]