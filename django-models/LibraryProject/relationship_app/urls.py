from django.urls import path
from .views import list_books, LibraryDetailView, CustomLoginView, RegisterView, CustomLogoutView

urlpatterns = [
    # Existing
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # New: Authentication
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
