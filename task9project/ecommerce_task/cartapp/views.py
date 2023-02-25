from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cart1,CartItem1
from shop_app.models import Product1
# Create your views here.
# def fun(request):
#     return HttpResponse("hai hello hw r u")
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product=Product1.objects.get(id=product_id)
    try:
        cart=Cart1.objects.get(cart_id=_cart_id(request))
    except Cart1.DoesNotExist:
        cart=Cart1.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item=CartItem1.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem1.DoesNotExist:
        cart_item=CartItem1.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cartapp:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=0):
    try:
        cart=Cart1.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem1.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total += (cart_item.quantity * cart_item.product.price)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=Cart1.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product1,id=product_id)
    cart_item=CartItem1.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:cart_detail')

def cart_delete(request,product_id):
    cart=Cart1.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product1,id=product_id)
    cart_item=CartItem1.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cartapp:cart_detail')



