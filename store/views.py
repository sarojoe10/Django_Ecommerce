from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request):

    products = Product.objects.all().filter(is_available=True)
    prodcuts_count = products.count()

    context = {
        'products':products,
        'product_count':prodcuts_count
    }
    return render(request,'store/store.html',context)