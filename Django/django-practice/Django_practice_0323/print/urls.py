from django.urls import path
from . import views

app_name = 'print'
urlpatterns = [
    path('number-print/<int:num>', views.number_print, name='number'),
    path('', views.index, name='index'),
]
