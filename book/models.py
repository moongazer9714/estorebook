from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Avg, Count
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms import ModelForm, TextInput, Textarea
from django.urls import reverse
from django.utils.safestring import mark_safe


class Category(models.Model):
    title = models.CharField(max_length=222, unique=True)
    keywords = models.CharField(max_length=222, unique=True)
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(max_length=222, blank=True)
    image = models.ImageField(upload_to='images/,', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})
    
    
class Product(models.Model):
    STATUS = (
        ('True','Mavjud'),
        ('False','Mavjud emas'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=222, unique=True)
    keywords = models.CharField(max_length=222, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    price = models. FloatField()
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    isbn = models.CharField(max_length=500)
    word = models.FileField(blank=True)
    pdf = models.FileField(blank=True)
    stu = models.FileField(blank=True)
    author = models.CharField(max_length=222)
    country = models.CharField(max_length=222)
    print = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})
    
    def image_tag(self):#admin qismda productga biriktirilgan rasmni productga kirmasdan turib ham ko'rsatib turishi kerak
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50">'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = 'Image'
    
    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg
    
    def countreview(self):
        reviews = Comment.objects.filter(product=self, status="True").aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt
    
    
class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=222, blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    STATUS = (
        ('True','Mavjud'),
        ('False','Mavjud emas'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=222, blank=True)
    comment = models.CharField(max_length=222, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=222, blank=True)
    status = models.CharField(max_length=222, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
    
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']  
    
