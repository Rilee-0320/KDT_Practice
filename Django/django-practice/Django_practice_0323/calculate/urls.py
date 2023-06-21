from django.urls import path
from . import views

app_name = 'calculate'
urlpatterns = [
    path('calculate/<int:num1>/<int:num2>', views.calculate, name='calculate'),
    path('', views.index, name='index')
]
