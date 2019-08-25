from django.shortcuts import render

# Create your views here.
from authors.models import Author


def authors_list(request):
    authors = Author.objects.all()
    return render(
        request,
        "authors/authors_list.html",
        {'authors': authors}
    )


def author_details(request, id):
    author = Author.objects.get(pk=id)
    return render(
        request,
        "authors/author_details.html",
        {'author': author}
    )
