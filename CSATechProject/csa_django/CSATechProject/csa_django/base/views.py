from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .models import *

def home(request):
    return render(request, "home.html")

@login_required(login_url="/login/")
def userPage(request):
    bookmarks = Bookmark.objects.all()
    form = NewBookmarkForm()
    context = {"bookmarks": bookmarks, "form": form}

    if request.method == "POST":
        '''
        form = NewBookmarkForm(user=request.user, title=request.POST.get('title'), link=request.POST.get('link'))
        if form.is_valid():
            form.save()
        '''
        bkmark = Bookmark(user=request.user, title=request.POST.get('title'), link=request.POST.get('link'))
        bkmark.save()
        return redirect('/user/')

    return render(request, "user.html", context)

@login_required(login_url="/login/")
def deleteBookmark(request, primary_key):
    bookmark = Bookmark.objects.get(id=primary_key)
    if request.method == "POST":
        bookmark.delete()
        return redirect('/user/')

    context = {'bookmark': bookmark}
    return render(request, 'delete.html', context)

@login_required(login_url="/login/")
def done(request, primary_key):
    bookmark = Bookmark.objects.get(id=primary_key)
    bookmark.completed = True
    bookmark.save()
    return redirect('/user/')

def authView(request):
    if request.user.is_authenticated:
        return redirect('/user/')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {user}')
                return redirect('/login/')
        else:
            form = CreateUserForm()
        return render(request, 'registration/signup.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/user/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/user/')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, 'registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login/')
