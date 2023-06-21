from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:artilce_pk>/delete/', views.delete, name='delete'),
]


# 메인 주소 articles/
# 상세 페이지 주소 articles/1/
