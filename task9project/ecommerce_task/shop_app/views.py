from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Category1,Product1
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# def index(request):
#     return HttpResponse("hai hello,this is test page")
def allProdCat(request,cat_slug=None):
    cat_page=None
    products_list=None
    if cat_slug!=None:
        cat_page=get_object_or_404(Category1,slug=cat_slug)
        products_list=Product1.objects.all().filter(category=cat_page,available=True)
    else:
        products_list =Product1.objects.all().filter(available=True)
    paginator=Paginator(products_list,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,"category.html",{'category':cat_page,'products':products})

def proDetail(request,cat_slug,product_slug):
    try:
        product1=Product1.objects.get(category__slug=cat_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product1})
