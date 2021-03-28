from django.conf.urls import url
from django.urls import path, include

from .views import BookDetailView, BookListView, AuthorListView, AuthorDetailView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<pk>/', AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
