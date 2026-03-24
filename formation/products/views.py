from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from products.models import Products

def products(request, *args, **kwargs):
    name = request.user
    number = 7
    mylist = [5, 2, 45, 23, 9, 11, 4]
    context = {
        "nom":str(name).upper,
        "numéro":number,
        "maList":mylist
    }
    #print(request.session)
    return render(request,template_name="index3.html", context=context, status=200)

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return HttpResponse("See my blog")

def product_list(request, *args, **kwargs):
    product = Products.objects.all()
    context = {
        'products':product
    }
    return render(request, template_name="products/detail.html", context=context)