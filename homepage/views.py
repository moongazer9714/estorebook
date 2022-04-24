from typing import Set
from django.db.models import query
from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import homepage
from homepage.models import Setting, Post, License, Images, ContactMessage, ContactForm, FAQ
from django.contrib import messages
from orderbook.models import ShopCart, Order
from book.models import Category, Product, Images, Comment
from .forms import SearchForm

def index(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    lic = License.objects.all()
    post = Post.objects.all()
    products_slider = Product.objects.all().order_by('id')[:6]
    products_latest = Product.objects.all().order_by('-id')[:6]
    products_picked = Product.objects.all().order_by('?')[:6]
    products_slider1 = Product.objects.all().order_by('?')[:6]
    
    page = "homepage"
    context = {
        'setting': setting,
        'page': page,
        'products_slider': products_slider,
        'products_latest': products_latest,
        'products_picked': products_picked,
        'products_slider1': products_slider1,
        'category': category,
        'post': post,
        'lic': lic,
    }
    return render (request, 'index.html', context)

def aboutus(request):
    setting = Setting.objects.all()
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
    }
    return render(request, 'about.html', context)
    
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi. Xabaringiz uchun rahmat!")
            return HttpResponseRedirect('/contact/')
    setting = Setting.objects.all()
    form = ContactForm
    category = Category.objects.all()
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request, 'contact.html', context)

def category_products(request, id, slug):
    category = Category.objects.all()
    catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {
        'category': category,
        'catdata': catdata,
        'products': products,
    }
    return render(request, 'category_products.html', context)

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)
            category = Category.objects.all()
            context = {
                'products': products,
                'query': query,
                'category': category,
            }
            return render(request, 'search.html', context)
    return HttpResponseRedirect('/')

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = []
        for rs in products:
            products_json = {}
            products_json = rs.title
            results.append(products_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    products_related = Product.objects.all().order_by('?')[:5]
    products_related1 = Product.objects.all().order_by('?')[:5]
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status=True)
    context = {
        'product': product,
        'category': category,
        'images': images,
        'comments': comments,
        'products_related': products_related,
        'products_related1': products_related1,
    }
    return render(request, 'product_detail.html', context)

def post(request):
    category = Category.objects.all()
    post = Post.objects.all()
    return render(request, 'post.html', {'category': category, 'post': post})

def lic(request):
    category = Category.objects.all()
    lic = License.objects.all()
    return render(request, 'lic.html', {'category': category, 'lic': lic})

def post_detail(request, id):
    category = Category.objects.all()
    product = Product.objects.all().order_by('?')[:8]
    post = Post.objects.get(pk=id)
    context = {
        'post': post,
        'category': category,
        'product': product,
    }
    return render(request, 'post_detail.html', context)

def lic_detail(request, id):
    category = Category.objects.all()
    product = Product.objects.all().order_by('?')[:8]
    lic = License.objects.get(pk=id)
    context = {
        'category': category,
        'product': product,
        'lic': lic,
    }
    return render(request, 'lic_detail.html', context)