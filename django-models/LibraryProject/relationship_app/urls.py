from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("",list_books,name="all_books"),
    path("",LibraryDetailView.as_view(),name="all_books_in_library")
]