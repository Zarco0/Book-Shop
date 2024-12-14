from django.shortcuts import render,redirect
from .models import tbl_Book,tbl_Author
from .forms import BookForm,AuthorForm

from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
# Create your views here.

def BookCreate(request):

    books = tbl_Book.objects.all()

    if request.method=='POST':

        form=BookForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form=BookForm()

    return render(request,'admin/book.html',{'form':form,'books':books})

def AuthorCreate(request):

    if request.method=='POST':

        form=AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form=AuthorForm()

    return render(request,'admin/author.html',{'form':form})

def BookDetails(request,book_id):

    book=tbl_Book.objects.get(id=book_id)

    return render(request,'admin/details.html',{'book':book})

def BookUpdate(request,book_id):

    book=tbl_Book.objects.get(id=book_id)

    if request.method=='POST':
        form=BookForm(request.POST,request.FILES,instance=book)

        if form.is_valid:
            form.save()
            return redirect('/')
        
    else:
        form=BookForm(instance=book)

    return render(request,'admin/update.html',{'form':form})


def BookDelete(request,book_id):
    book=tbl_Book.objects.get(id=book_id)

    if request.method=='POST':
        book.delete()
        return redirect('/')
    
    return render(request,'admin/delete.html',{'book':book})

def listBook(request):
    books=tbl_Book.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_page)

    return render(request,'admin/listbook.html',{'books':books,'page':page})


def index(request):
    return render(request,'admin/base.html')


def SearchBook(request):

    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=tbl_Book.objects.filter(Q(title__icontains=query))

    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'admin/search.html',context)
