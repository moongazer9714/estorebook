from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.forms import ModelForm
from book.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.product.title
    
    @property
    def price(self):
        return (self.product.price)
    
    @property
    def amount(self):
        return (self.quantity * self.product.price)
    
    
class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
        
        
class Order(models.Model):
    STATUS = (
        ('New','Yangi'),#yangi buyurtma
        ('Accepted','Qabul qilingan'),#klient qabul qildi
        ('OnShipping','Yetkazib berishga'),#yetkazib berishga tayyorlanyabti
        ('Completed','Tugallangan'),#buyurtma tugallangan
        ('Cancelled','Bekor qilingan'),#buyurtma bekor qilingan
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    code = models.CharField(max_length=5,editable=False)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    phone = models.CharField(max_length=20,blank=True)
    address = models.CharField(blank=True,max_length=255)
    city = models.CharField(blank=True,max_length=255)
    country = models.CharField(blank=True,max_length=255)
    total = models.FloatField()
    status = models.CharField(max_length=15,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=25)
    adminnote = models.CharField(max_length=100,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'city', 'country']
        
        
class OrderProduct(models.Model):
    STATUS = (
        ('New','Yangi'),
        ('Accepted','Qabul qilingan'),
        ('Cancelled','Bekor qilingan'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # title = models.CharField(max_length=222)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=222, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.title
        
