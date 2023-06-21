from django.urls import path
from . import views

PK = 'account_book_pk'

app_name = 'accountbooks'
urlpatterns = [
    path('', views.index, name='index'),
    path(f'<int:{PK}>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path(f'<int:{PK}>/edit/', views.edit, name='edit'),
    path(f'<int:{PK}>/update/', views.update, name='update'),
    path(f'<int:{PK}>/delete/', views.delete, name='delete'),
    path(f'<int:{PK}>/copy/', views.copy, name='copy'),
]
