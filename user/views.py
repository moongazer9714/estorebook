from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from homepage.models import FAQ 
from orderbook.models import Order, OrderProduct
from book.models import Category, Comment
from user.models import UserProfile, User
from user.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm



# def index(request):
#     return HttpResponse("hello")

@login_required(login_url='/login_form/')
def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'category':category,
        'profile':profile,
    }
    return render(request, 'user_profile.html', context)

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            current_user=request.user
            profile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = profile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error! User name or Password is incorrect")
            return HttpResponseRedirect('/user/login_form/')
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request, 'login_form.html', context)

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user=request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'images/users/user.png'
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/user/signup_form/')
    form = SignUpForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'signup_form.html', context)

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login_form/')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your account has been updated')
            return HttpResponseRedirect('/user/')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category':category,
            'user_form':user_form,
            'profile_form':profile_form,
           
        }
        return render(request,'user_update.html',context)

@login_required(login_url='/login_form/')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user/')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/user_password/')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'category': category, 'form': form})
    
@login_required(login_url='/login_form/')
def user_orders(request):
    current_user = request.user
    orders = Order.objects.filter(user_id = current_user.id)
    context = {
        'orders': orders,
    }
    return render(request, 'user_orders.html', context)

@login_required(login_url='/login_form/')
def user_order_detail(request, id):
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {
        'order': order,
        'current_user': current_user,
        'orderitems': orderitems,
    }
    return render(request, 'user_order_detail.html', context)

@login_required(login_url='/login_form/')
def user_order_product(request):
    #category = Category.objects.all()
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id).order_by('-id')
    context = {
        #'category': category,
        'order_product': order_product,
    }
    return render(request, 'user_order_product.html', context)

@login_required(login_url='/login_form/')
def user_order_product_detail(request, id, oid):
    #category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitems = OrderProduct.objects.filter(id=id, user_id=current_user.id)
    context = {
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'user_order_product_detail.html', context)

def user_comments(request):
    #category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        #'category': category,
        'comments': comments,
    }
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login_form/')
def user_delete_comments(request, id):
    current_user = request.user
    Comment.objects.filter(user_id=current_user.id, id=id).delete()
    messages.success(request, 'Comment Deleted...')
    return HttpResponseRedirect('/user/user_comments/')

def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.filter(status='True').order_by('ordernumber')
    context = {
        'category': category,
        'faq': faq,
    }
    return render(request, 'faq.html', context)


