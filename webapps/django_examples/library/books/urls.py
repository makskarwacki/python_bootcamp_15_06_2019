from django.urls import path

from books.views import books_list, book_details

urlpatterns = [
    path('', books_list, name="books"),
    path('<int:id>', book_details, name="book"),
]