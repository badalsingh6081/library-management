from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import book_form
from django.contrib import messages
from . models import book
from django.core.paginator import Paginator
# Create your views here.


def add_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = book_form(request.POST)
            if form .is_valid():
                form.save()
                messages.success(request, 'Successfully Book Added in Library')
                return redirect('/showbook/')
        else:
            form = book_form()
        return render(request, 'book/add_book.html', {'form': form})
    else:
        return redirect('/login/')


def show_book(request):
    if request.user.is_authenticated:
        fm = book.objects.all().order_by('id')
        paginator = Paginator(fm, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'book/showbook.html',  {'page_obj': page_obj, 'book': 'active'})
    else:
        messages.warning(request, 'Please Login First')
        return redirect('/login/')


def edit_book(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = book.objects.get(pk=id)
            fm = book_form(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Book Update Successfully')
                return redirect('/showbook/')
        else:
            pi = book.objects.get(pk=id)
            fm = book_form(instance=pi)
        return render(request, 'book/editbook.html', {'books': fm})
    else:
        return redirect('/login/')


def delete_book(request, id):
    if request.user.is_authenticated:
        pi = book.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'Book Deleted Successfully')
        return redirect('/showbook/')
    else:
        return redirect('/login/')


def search_by_title(request):
    context = {'search': 'active'}
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            bk = book.objects.filter(title__icontains=title).order_by('id')
            paginator = Paginator(bk, 4)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            if page_obj is not None:
                return render(request, 'book/showbook.html', {'page_obj': page_obj})
            else:
                messages.warning(request, 'Please enter Your choice')
                return render(request, 'book/searchtitle.html',)
        return render(request, 'book/searchtitle.html', context)
    else:
        return redirect('/login/')


def search_by_author(request):
    context = {'search':'active'}
    if request.user.is_authenticated:
        if request.method =='POST':
            author = request.POST.get('author')
            bk = book.objects.filter(author__icontains=author).order_by('id')
            paginator = Paginator(bk, 4)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            if page_obj is not None:
                return render(request, 'book/showbook.html', {'page_obj': page_obj})
            else:
                messages.warning(request, 'Please enter Your choice')
                return render(request, 'book/searchauth.html',)

        return render(request, 'book/searchauth.html',context)
    else:
        return redirect('/login/')



def search_by_cat(request):
    context = {'search':'active'}  
    if request.user.is_authenticated:
        if request.method =='POST':
            category = request.POST.get('category')
            bk = book.objects.filter(category__icontains=category).order_by('id')
            paginator = Paginator(bk, 4)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            if page_obj is not None:
                return render(request, 'book/showbook.html', {'page_obj': page_obj})
            else:
                messages.warning(request, 'Please enter Your choice')
                return render(request, 'book/searchcat.html',)
        return render(request, 'book/searchcat.html',context)
    else:
        return redirect('/login/')
