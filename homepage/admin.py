from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Setting)
admin.site.register(Post)
admin.site.register(License)
admin.site.register(ContactMessage)
admin.site.register(FAQ)