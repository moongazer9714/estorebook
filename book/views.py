from django.db import models
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from book.models import Category, Product, Images, Comment, CommentForm

def index(request):
    return HttpResponse("my product page")

def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id=id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Sizning kommentariyangiz yuborildi, qiziqish uchun rahmat")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)        