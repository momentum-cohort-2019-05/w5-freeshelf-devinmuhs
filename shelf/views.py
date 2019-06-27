from django.shortcuts import render

# Create your views here.
from shelf.models import Category, Book

def index(request):
    """View function for home page of site."""

    book_list = Book.objects.all()
    category_list = Category.objects.all()

    context = {
        'book_list': book_list,
        'category_list': category_list,
    }

    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class CategoryDetailView(generic.DetailView):
    model = Category