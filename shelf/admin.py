from django.contrib import admin

# Register your models here.
from shelf.models import Book, Category

admin.site.register(Book)
admin.site.register(Category)