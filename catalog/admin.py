from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from .models import Genre, Author, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)


class AuthorInstanceInline(admin.TabularInline):
    model = Book
    extra = 0
    # fields = ['title']
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorInstanceInline]

# Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )