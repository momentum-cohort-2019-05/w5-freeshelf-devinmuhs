from django.contrib import admin

# Register your models here.
from shelf.models import Book, Category

# admin.site.register(Book)
admin.site.register(Category)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'add_date', 'display_category')

