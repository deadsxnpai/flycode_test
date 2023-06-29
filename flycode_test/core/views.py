from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Book, Comment
from .forms import CommentForm, BookForm


def index(request):
    return render(request, 'core/index.html')

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'core/author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.filter(archived=False)
    return render(request, 'core/book_list.html', {'books': books})

def author_books(request, author_id):
    selected_author = Author.objects.get(id=author_id) 
    books = selected_author.books.filter(archived=False)
    return render(request, 'core/author_books.html', {'author': selected_author, 'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    authors = book.authors.all()
    comments = Comment.objects.filter(book=book)
    return render(request, 'core/book_detail.html', {'book': book, 'comments': comments, 'authors':authors})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(f'http://127.0.0.1:8000/books/{book_id}', book_id=book_id)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'core/edit_book.html', {'form': form, 'book': book})

def change_archived_flag(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.archived = not book.archived
    book.save()
    return redirect('core/book_detail', book_id=book_id)

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('http://127.0.0.1:8000/books')
    
def create_comment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect(f'http://127.0.0.1:8000/books/{book_id}', book.id)
    else:
        form = CommentForm()
    return render(request, 'core/create_comment.html', {'form': form, 'book': book})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(f'http://127.0.0.1:8000/books/{comment.book_id}', comment.book.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'core/edit_comment.html', {'form': form, 'comment': comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    book_id = comment.book.id
    comment.delete()
    return redirect(f'http://127.0.0.1:8000/books/{book_id}', book_id)


