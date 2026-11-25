from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    
    c=Category.objects.all()
    p=Product.objects.all()

    q = (request.GET.get("q") or "").strip()
    category_id = request.GET.get("category")
    a= int(category_id) if category_id else None
    product = Product.objects.all()
    qs =Product.objects.select_related("category").all()
    if a:
        qs = qs.filter(category_id=a)
    paginator = Paginator(qs, 3)
    page = paginator.get_page(request.GET.get('page', 1))
    if q:
        product = product.filter(
                Q(product__icontains=q) |
                Q(category__name__icontains=q)
            )

        
        if category_id:
            products = products.filter(category_id=category_id)

    context = {
          
            "mahsulot": product,
            "category": Category.objects.all(),
            "query": q,
            "active_category":a,
            "paginator":paginator,
            "page":page
    }

    
    return render(request,"index.html",context)