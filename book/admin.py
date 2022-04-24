from django.contrib import admin
import admin_thumbnails
from book.models import *

@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1 

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Comment)