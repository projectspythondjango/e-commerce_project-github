from django.shortcuts import render
from shop_app.models import Product1
from django.db.models import Q

# Create your views here.
def searchresult(request):
    query=None
    products=None
    if request.method == "GET":
        query=request.GET.get('q')
        products=Product1.objects.all().filter(Q(name__contains=query)| Q(description__contains=query))
    return render(request,'search.html',{'query':query,'products':products})
