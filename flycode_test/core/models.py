from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', blank=True, default=None)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comments')
    text = models.TextField()

    def __str__(self):
        return f'Комментарий на книгу {self.book} от {self.user}'