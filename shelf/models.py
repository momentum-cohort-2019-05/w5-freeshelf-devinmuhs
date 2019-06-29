from django.db import models

# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

class Category(models.Model):
    """Model representing a book category."""
    name = models.CharField(max_length=200, help_text='Enter a book category (e.g. Javascript, Python)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('category-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'categories'

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    url_address = models.URLField(max_length=200, unique=True, help_text='Enter the url for this book')
    add_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text='Select a category for this book')
    class Meta:
        ordering = ['-add_date']

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return self.url_address

    def display_category(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])
    
    display_category.short_description = 'Category'

class Favorite(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, unique=False, on_delete=models.CASCADE)