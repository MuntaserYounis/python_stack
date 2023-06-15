from django.shortcuts import render,redirect
from .models import Book,Author

def index(request):
    context = {"books":Book.objects.all()}
    return render(request,'index.html',context)

def authors(request):
    return render(request,'authors.html')

def add_book(request):
    Book.objects.create(title = request.POST['book_title'],desc = request.POST['book_desc'])
    return redirect('/')

def view(request,id):
    book = Book.objects.get(id = id)
    authors = book.authors.all()
    all_authors = Author.objects.all()
    context = {'book':book, 
                'authors' : authors,
                'all_authors':all_authors}
    return render(request,'books.html',context)

def adding_author(request):
    author = Author.objects.get(id = request.POST['add_author'])
    this_book = Book.objects.get(id = request.POST['book_id'])
    author.books.add(this_book)
    return redirect('view',id=this_book.id)