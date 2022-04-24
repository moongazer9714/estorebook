from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_form/', views.login_form, name='login_form'),
    path('signup_form/', views.signup_form, name='signup_form'),
    path('user_update/', views.user_update, name='user_update'),
    path('user_password/', views.user_password, name='user_password'),
    path('user_orders/', views.user_orders, name='user_orders'),
    path('user_order_detail/<int:id>/', views.user_order_detail, name='user_order_detail'),
    path('user_order_product/', views.user_order_product, name='user_order_product'),
    path('user_order_product_detail/<int:id>/<int:oid>/', views.user_order_product_detail, name='user_order_product_detail'),
    path('user_comments/', views.user_comments, name='user_comments'),
    path('faq/', views.faq, name='faq'),
    path('logout/', views.logout_func, name='user_logout'),
    path('user_delete_comments/<int:id>/', views.user_delete_comments, name='user_delete_comments'),
]