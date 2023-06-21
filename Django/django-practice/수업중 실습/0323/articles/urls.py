from django.urls import path
# 명시적 상대경로(django 권장사항)
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.details, name='details'),
    path('hello/<str:name>', views.hello, name='hello'),
]
