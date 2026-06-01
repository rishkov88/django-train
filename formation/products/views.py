from pydoc import text
from typing import Text

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from products.models import Products
from .form import ProductForm, RowProductForm


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

def productCreate(request):
    form = ProductForm(request.POST or None)
    Text=""
    if form.is_valid():
        form.save()
        form = ProductForm()
        Text = "Products succesfully add"
    return render(request, "products/create.html", {'form':form, 'msg':Text})

def modifier(request, my_id):
    # last = Products.objects.all().count()
    obj = get_object_or_404(Products, id=my_id)
    # try:
    #     obj = Products.objects.get(id=my_id)
    # except Products.DoesNotExist:
    #     raise Http404("Cet article n'existe pas")
    form = ProductForm(request.POST or None, instance=obj)
    Text=""
    if form.is_valid():
        form.save()
        form = ProductForm()
        Text = "Your modification was succefully done!"
    return render(request, "products/update.html", {'form':form, 'msg':Text, "my_id":my_id})

def table(request):
    obj = Products.objects.all()
    return render(request, "products/table.html", {'obj': obj})

def deleteProduct(request, my_id):
    obj = get_object_or_404(Products, id=my_id)
    name = obj.name
    if request.method == "POST":
        obj.delete()
        return redirect('table')
    return render(request, "products/delete.html", {"name":name, "my_id":my_id})



 













# def productCreate(request):
#     # if request.method == "POST"
#     if request.POST:
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         price = request.POST.get("price")
#         image = request.POST.get("image")
#         if request.POST.get("status") == "active":
#             status = True
#         else:
#             status = False
#         newProduct = Products.objects.create(name=name, description=description, price=price, image=image, status=status)
#         newProduct.save()
#         message = "Your product was save successfully"
#         # print(request.POST)
#     return render(request, "products/create.html", context={"message":message})


# def productCreate(request):
#     form = RowProductForm()
#     message = ""
#     if request.POST:
#         form = RowProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             new = Products.objects.create(**form.cleaned_data)
#             new.save()
#             form = RowProductForm()
#             message = "Your product was save successfully"
#     return render(request, 'products/create.html', {"form": form, 'message':message})


