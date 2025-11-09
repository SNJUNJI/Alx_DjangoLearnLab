from django.urls import path
from . import views

urlpatterns = [
    # Existing paths...
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
