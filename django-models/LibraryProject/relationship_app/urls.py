from django.urls import path
from relationship_app.views import list_books ,all_books_in_library

urlpatterns = [
    path("",list_books,name="all_books"),
    path("",all_books_in_library.as_view(),name="all_books_in_library")
]