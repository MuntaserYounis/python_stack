from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt



def index(request):
    return render(request,'index.html')
# Create your views here.

def register(request):
    print('hi')
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        request.session['username'] = first_name +" " + last_name
        request.session['status'] = 'registered'
        
        
        user = User.objects.create(first_name = first_name, last_name = last_name, email= email, password = pw_hash)
        request.session['user_id'] = user.id
    return redirect('/books')

def login(request):
    errors2 = User.objects.login_validator(request.POST)
    if len(errors2 ) > 0:
        for key,value in errors2.items():
            messages.error(request, value)
        return redirect('/')
    
    user= User.objects.filter(email = request.POST['email2'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password2'].encode(),logged_user.password.encode()):
            request.session['username'] = logged_user.first_name
            request.session['status'] = 'logged in'
            request.session['user_id'] = logged_user.id
            return redirect('/books')
        print('Wrong Password')


def logout(request):
    del request.session['username']
    del request.session['status']
    request.session.flush()
    return redirect('/')

def books(request):
    user = User.objects.get(id = request.session['user_id'])
    books = Book.objects.all()
    context = {
        'books' : books,
        'user' : user,
    }
    return render(request,'adding_book.html',context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
            return redirect('/books')
    else:

        title = request.POST['title']
        desc = request.POST['desc']
        creator = User.objects.get(id = request.session['user_id'])
        
        new_book = Book.objects.create(title = title , desc = desc,uploaded_by =creator )
        new_book.users_who_like.add(creator)
        request.session['book_id'] = new_book.id
        return redirect(f'/books/{new_book.id}')

def book_view(request,book_id):
    the_user = User.objects.get(id = request.session['user_id'])
    book_inview = Book.objects.get(id = book_id)
    if book_inview.uploaded_by.id == the_user.id:
        context ={
            'the_book' : book_inview,
            'creator' : the_user
        }
        return render(request,'book_view_edit.html',context)
    else:
        context ={
            'the_book' : book_inview,
            'user' : the_user
        }
        return render(request,'book_view.html',context)