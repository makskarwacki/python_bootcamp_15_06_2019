from django.urls import path

from authors.views import authors_list, author_details

urlpatterns = [
    path('', authors_list, name="authors"),
    path('<int:id>', author_details, name="author"),
]