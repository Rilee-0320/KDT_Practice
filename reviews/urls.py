from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:review_pk>', views.detail, name='detail'),
    path('update/<int:review_pk>/', views.update, name='update'),
    path('detail/<int:review_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('detail/<int:review_pk>/comment_delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
]
