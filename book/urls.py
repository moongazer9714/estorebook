
from django.urls import path, include
from book import views 

urlpatterns = [
    path('addcomment/<int:id>',views.addcomment,name='addcomment'),
    path('', views.index, name="index"),
]