from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from UserApp import views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('user', views.users, name='user_list'),
    path('user/<str:id>/', views.users, name='user_detail'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    # Endpoint para renovar token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]