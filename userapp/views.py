from django.shortcuts import render,redirect
from django.urls import reverse
from myBook .models import tbl_Book
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage
from .models import Cart,Cartitem
from django.contrib import messages
from django.conf import settings

import stripe
# Create your views here.

def bookView(request):

    books = tbl_Book.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_page)

    return render(request,'user/listbook.html',{'books':books,'page':page})


def BookDetails(request,book_id):

    book=tbl_Book.objects.get(id=book_id)

    return render(request,'user/details.html',{'book':book})


def SearchBook(request):

    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=tbl_Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'user/search.html',context)

def addToCart(request,book_id):
    book=tbl_Book.objects.get(id=book_id)

    if book.quantity>0:
        cart,created = Cart.objects.get_or_create(user=request.user)
        cart_item,item_created=Cartitem.objects.get_or_create(cart=cart,book=book)

        if not item_created:
            cart_item.quantity+=1
            cart_item.save()

    return redirect('webuser:viewcart')



def view_cart(request):
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    cart_item = Cartitem.objects.all()
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    total_items = cart_items.count()
    context = {
                'cart_items': cart_items,
                'cart_item': cart_item,
                'total_price': total_price,
                'total_items': total_items
            }

    return render(request,'user/cart.html',context)


def increse_quantity(request,item_id):
    cart_item=Cartitem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:

        cart_item.quantity +=1
        cart_item.save()

    return redirect('webuser:viewcart')

def decrease_quantity(request,item_id):
    cart_item=Cartitem.objects.get(id=item_id)
    if cart_item.quantity > 1:

        cart_item.quantity -=1
        cart_item.save()

    return redirect('webuser:viewcart')

def remove_from_cart(request,item_id):

    try:
        cart_item=Cartitem.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass
    return redirect('webuser:viewcart')

def create_checkout_session(request):
    cart_items=Cartitem.objects.all()

    if cart_items:
        stripe.api_key=settings.STRIPE_SECRET_KEY

        if request.method=='POST':

            line_items=[]
            for cart_item in cart_items:
                if cart_item.book:
                    line_item={
                        'price_data':{
                            'currency':'INR',
                            'unit_amount':int(cart_item.book.price * 100),
                            'product_data':{
                                'name':cart_item.book.title
                            },
                        },
                        'quantity':1
                    }
                    line_items.append(line_item)

            if line_items:

                checkout_session=stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url=request.build_absolute_uri(reverse('webuser:success')),
                    cancel_url=request.build_absolute_uri(reverse('webuser:cancel'))
                )
                return redirect(checkout_session.url,code=303)
            
def success(request):
    cart_items=Cartitem.objects.all()

    for cart_item in cart_items:
        product=cart_item.book
        if product.quantity >= cart_item.quantity:
            product.quantity-=cart_item.quantity
            product.save()
    
    cart_items.delete()

    return render(request,'user/success.html')

def cancel(request):
    return render(request,'user/cancel.html')