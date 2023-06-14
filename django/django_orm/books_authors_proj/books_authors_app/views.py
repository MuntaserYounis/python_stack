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

def view(request):
    context = {'books':Book.objects.all()}
    return render(request,'')

