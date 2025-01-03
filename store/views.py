from django.shortcuts import render, get_object_or_404,redirect
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.
def store(request,category_slug=None):

    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True).order_by('id')
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products,1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()

    context = {
        'products':paged_products,
        'product_count':products_count
    }
    return render(request,'store/store.html',context)


def product_detail(request,category_slug,product_slug):
    try:
        single_prodcut = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_prodcut).exists()
    except Exception as e:
        raise e


    context = {
        'single_product' : single_prodcut,
        'in_cart' : in_cart
    }
    return render(request,'store/product_detail.html',context)


def search(request):
    products=''
    product_count=0
    keyword=''
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products=Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword)|Q(category__category_name__icontains=keyword))
            product_count=products.count()
        else:
            return redirect('store')
    context={
        'products' : products,
        'product_count' : product_count,
        'keyword' : keyword

    }
    return render(request,'store/store.html',context)
