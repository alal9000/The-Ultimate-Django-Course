from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction

# Create your views here.

# def calculate():
#     x =1
#     y =2
#     return x

# def sayHello(request):
#     x = calculate()
#     return render(request, 'hello.html', {'name': 'Mosh'})

def sayHello(request):
    product = Product.objects
    

    return render(request, 'hello.html', {'name': 'Mosh', 'tags': list()})
    