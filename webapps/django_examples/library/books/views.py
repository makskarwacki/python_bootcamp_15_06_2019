from django.shortcuts import render

# Create your views here.
from books.models import Book


def books_list(request):
    books = Book.objects.all()
    return render(
        request,
        "books/books_list.html",
        {'books': books}
    )


def book_details(request, id):
    book = Book.objects.get(pk=id)
    return render(
        request,
        "books/book_details.html",
        {'book': book}
    )
