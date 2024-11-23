from django.urls import path, re_path
from UserApp import views

urlpatterns = [
    # Usando path() para rotas simples
    path('user', views.users, name='user_list'),
    # Usando re_path() para incluir parâmetros com regex
    re_path(r'user/<str:id>/', views.users, name='user_detail'),
]