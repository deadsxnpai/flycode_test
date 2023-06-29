from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='index'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/change_archived_flag/', views.change_archived_flag, name='change_archived_flag'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/create/<int:book_id>', views.create_comment, name='create_comment'),
]