from django.contrib import admin
from .models import Author, Book, Comment
from django.db.models import Count
from django import forms

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_authors','comment_count')

    def comment_count(self, obj):
        return obj.comment_count

    comment_count.short_description = 'Кол-во комментариев'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comment_count=Count('book_comments'))
        return queryset
    
    def display_authors(self, obj):
        return ', '.join([author.name for author in obj.authors.all()])

    display_authors.short_description = 'Автор(ы)'

class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'books': forms.HiddenInput(),
        }

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','book_count','comment_count')

    def comment_count(self, obj):
        return obj.comment_count

    comment_count.short_description = 'Кол-во комментариев'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comment_count=Count('book_comments'))
        return queryset

    def book_count(self, obj):
        return obj.books.count()

    book_count.short_description = 'Кол-во книг'  

    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
