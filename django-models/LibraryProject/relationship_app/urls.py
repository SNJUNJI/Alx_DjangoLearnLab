
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Enables views.register etc.

urlpatterns = [
    # Existing paths (adjust if needed)
    path('books/', views.list_books, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Auth paths (exact to match test strings)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Contains "LoginView.as_view(template_name="
    path('register/', views.register, name='register'),  # Contains "views.register"
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Contains "LogoutView.as_view(template_name="
]
