from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.aboutus, name="about"),
    path('contact/', views.contactus, name='contact'),
    path('category/<int:id>/<slug:slug>/', views.category_products, name='category_products'),
    path('search/', views.search, name='search'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('post/', views.post, name='post'),
    path('lic/', views.lic, name='lic'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('lic/<int:id>/', views.lic_detail, name='lic_detail'),
    path('search_auto/', views.search_auto, name='search_auto'),
    
] 